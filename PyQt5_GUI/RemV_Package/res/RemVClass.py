import sys, FirstGui, functions
from PyQt5.QtGui import QPixmap, QIcon, QPalette, QBrush
from PyQt5.QtWidgets import QMainWindow, QApplication


def loadQss():
    with open(r"qss.txt", "r") as f:
        return f.read()


class RemV(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = FirstGui.Ui_MainWindow()
        FirstGui.Ui_MainWindow.setupUi(self.ui, self)
        # 添加主窗口背景图
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./image/background_3")))
        self.setPalette(palette)
        # 给各个按钮加对应图标
        self.ui.uploadButton.setIcon(QIcon(r"./image/upload.png"))
        self.ui.MemorizeBtn_0.setIcon(QIcon(r"./image/brain.png"))
        self.ui.QuizBtn_0.setIcon(QIcon(r"./image/quiz.png"))

        # 给列表添加 spacing
        self.ui.bookListWidget.setSpacing(20)
        self.ui.lessonListWidget.setSpacing(10)
        self.ui.meaningListWidget.setSpacing(5)
        self.ui.wordListWidget.setSpacing(5)

        # 给列表添加 点击事件
        self.ui.bookListWidget.itemClicked.connect(self.bookClicked)
        self.ui.lessonListWidget.itemClicked.connect(self.lessonClicked)

        # 初始化数据
        # 保存book路径的list
        self.pathList = [r"./word_Repository/TestMaterial.xlsx", r"./word_Repository/SatVocabulary.xlsx"]

        # 总共有多少课
        self.lessonNum = 0
        # 装每节课的列表
        self.lessonList = []
        self.currentBook = ""
        self.currentLesson = 0
        self.currentSeq = "List Order"
        self.currentIndex = 0
        # words list for a specific book
        self.wordsLFSB = []
        # words of all books
        self.wordsOAB = {}
        # 当前数据
        self.currentWord = ""
        self.currentPOS = ""
        self.currentMeaning = ""
        self.countRound = 0
        self.lessonLen = 0
        # 本次学习数量
        self.nowNum = 0
        # 共学习数量
        self.accumulativeNum = 0
        # 控制是翻译还是显示原意思
        self.controlTranslate = True
        self.totalStudyTime = 0
        self.lastProgress = ""
        self.randomSet = set()
        self.noWrongTime = True

        # 调用方法
        # 解析已存在的excel
        self.parseAllBooks(self.pathList)

    def bookClicked(self, item):
        """
        bookListWidget的单机事件
        :param item: (点击自动提供) PyQt5.QtWidgets.QListWidgetItem object
        :return:
        """
        # self.ui.bookListWidget.row(item) 是获取所以索引
        # 更新 currentBook
        self.currentBook = self.pathList[self.ui.bookListWidget.row(item)]
        # 更新这本书对应的课程
        self.setLessons(self.currentBook)

    def lessonClicked(self, item):
        """
        lessonListWidget的单机事件
        :param item:(点击自动提供) PyQt5.QtWidgets.QListWidgetItem object
        :return:
        """
        # 判断有没有选择书
        if self.currentBook == "":
            return
        # 使左半边变成enabled
        self.ui.stackedWidget.setEnabled(True)
        # 更新 currentLesson, lessonLen
        self.currentLesson = self.ui.lessonListWidget.row(item)
        self.lessonLen = len(self.wordsOAB[self.currentBook][self.currentLesson])

        # 清空 wordListWi 和 meaningListWid
        self.ui.wordListWidget.clear()
        self.ui.meaningListWidget.clear()

        self.setOverViewScene()

    def setOverViewScene(self):
        """
        把OverViewScene设置好
        :return: None
        """
        # 根据currentBook 和 currentLesson 填补单词和意思
        for i in range(self.lessonLen):
            self.ui.wordListWidget.addItem(
                self.wordsOAB[self.currentBook][self.currentLesson][i][0]
            )
            if self.wordsOAB[self.currentBook][self.currentLesson][i][1][0] is not None:
                self.ui.meaningListWidget.addItem(
                    str(self.wordsOAB[self.currentBook][self.currentLesson][i][1][0]) +
                    self.wordsOAB[self.currentBook][self.currentLesson][i][1][1]
                )
            else:
                self.ui.meaningListWidget.addItem(
                    self.wordsOAB[self.currentBook][self.currentLesson][i][1][1]
                )

    def parseAllBooks(self, pathList):
        """
        解析所有的path
        :param pathList: 包含许多path的一个list
        :return: None
        """
        self.ui.bookListWidget.clear()
        for each in pathList:
            self.parseFile(each)

    def parseFile(self, path):
        """
        更新bookList, 获取每个path里的excel文件
        :param path:
        :return:
        """
        # 处理 bookList
        tmpList1 = []
        tmpList1 += functions.getBookNames([path])
        # 在 bookList 里添加书籍的名词
        self.ui.bookListWidget.addItems(tmpList1)

        # # 处理 lessonList
        # self.setLessons(path)

        # 处理words 把SAT单词书 分成好几节课 然后把SAT这真本书 放到wordsOAB 里面 名字与书的内容
        self.wordsLFSB = (functions.divideIntoLessons(functions.excelParse(path)))

        # 把每本书的链接 和 内容 用字典储存
        self.wordsOAB.update({path: self.wordsLFSB})

        # # 保存数据
        # self.saveData()

    def setLessons(self, path):
        """
        把一本书分成20为一课的许多课程，并添加到 lessonList 里
        :param path
        :return: None
        """
        # 初始化
        self.ui.lessonListWidget.clear()
        # 每次都需要初始化 lessonList 不然换书的时候就崩了
        tmpList2 = functions.excelParse(path)
        self.lessonNum = functions.getLessonNum(tmpList2)
        self.lessonList = []
        for i in range(1, self.lessonNum + 1):
            self.lessonList.append("Lesson " + str(i))
        self.ui.lessonListWidget.addItems(self.lessonList)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = RemV()
    win.setStyleSheet(loadQss())
    win.show()

    sys.exit(app.exec_())
