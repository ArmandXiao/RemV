import sys, FirstGui, functions, os, getTranslationFromYouDao
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QPalette, QBrush
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog


def loadQss():
    with open(r"qss.txt", "r") as f:
        return f.read()


class RemV(QMainWindow):
    def __init__(self):
        super().__init__()
        os.chdir(os.getcwd())
        self.ui = FirstGui.Ui_MainWindow()
        FirstGui.Ui_MainWindow.setupUi(self.ui, self)

        # 更改图片尺寸
        self.image = QPixmap(r"res/image/background_3")
        self.image = self.image.scaled(1260, 835, Qt.IgnoreAspectRatio, Qt.FastTransformation)

        # 添加主窗口背景图
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap(self.image)))
        self.setPalette(palette)

        # 先disable
        self.ui.stackedWidget.setEnabled(False)
        self.ui.stackedWidget.setCurrentIndex(0)

        # 给各个按钮加对应图标
        self.ui.uploadButton.setIcon(QIcon(r"res/image/upload_2.png"))
        self.ui.MemorizeBtn_0.setIcon(QIcon(r"res/image/brain.png"))
        self.ui.MenuBtn_1.setIcon(QIcon(r"res/image/home_2.png"))
        self.ui.QuizBtn_0.setIcon(QIcon(r"res/image/quiz.png"))
        self.ui.QuizBtn_1.setIcon(QIcon(r"res/image/quiz.png"))
        self.ui.helpBtn.setIcon(QIcon(r"res/image/question.png"))
        self.ui.translateBtn.setIcon(QIcon(r"res/image/translate.png"))
        self.ui.backBtn.setIcon(QIcon(r"res/image/back_2.png"))
        self.ui.NextBtn.setIcon(QIcon(r"res/image/next_2.png"))
        self.ui.showBtn.setIcon(QIcon(r"res/image/word.png"))

        # 给列表添加 spacing
        self.ui.bookListWidget.setSpacing(20)
        self.ui.lessonListWidget.setSpacing(10)
        self.ui.meaningListWidget.setSpacing(5)
        self.ui.wordListWidget.setSpacing(5)

        # 给列表添加 点击事件
        self.ui.bookListWidget.itemClicked.connect(self.bookClicked)
        self.ui.lessonListWidget.itemClicked.connect(self.lessonClicked)

        # uploadBtn 添加点击事件
        self.ui.uploadButton.clicked.connect(self.uploadBtnClicked)

        # 给 memorize 和 quiz 添加事件 切屏事件
        self.ui.MemorizeBtn_0.clicked.connect(self.changeScene_1)

        # next, back, translate, show 添加点击事件
        self.ui.NextBtn.clicked.connect(self.next)
        self.ui.backBtn.clicked.connect(self.back)
        self.ui.translateBtn.clicked.connect(self.translate)
        self.ui.showBtn.clicked.connect(self.updateWord)

        # 初始化数据
        # 保存book路径的list
        self.pathList = [r"res/word_Repository/TestMaterial.xlsx", r"res/word_Repository/SatVocabulary.xlsx"]

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

        # 调高透明度
        self.ui.wordListWidget.setStyleSheet("background-color: rgb(255,255,255)")
        self.ui.meaningListWidget.setStyleSheet("background-color: rgb(255,255,255)")

    def setOverViewScene(self):
        """
        把OverViewScene设置好
        :return: None
        """
        # enable
        self.ui.wordListWidget.setEnabled(True)
        self.ui.lessonListWidget.setEnabled(True)

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

    def uploadBtnClicked(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "上传文件", "./", "Excel (*.xlsx)")  # 设置文件扩展名过滤,注意用双分号间隔
        # _ 是返回的type 如果是excel 就返回 "Excel (*.xlsx)"
        if _ != "":
            self.parseFile(filePath)
            # 查重
            if filePath not in self.pathList:
                self.pathList.append(filePath)
        else:
            print("上传动作取消")

    def changeScene_1(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.bookListWidget.setEnabled(False)
        self.ui.lessonListWidget.setEnabled(False)

        # 把第一个元素更新
        self.updateWord(0)
        self.ui.countBrowser_1.setText("  1")
        self.ui.backBtn.setEnabled(False)
        self.ui.showBtn.setVisible(False)

    def updateWord(self, index):
        """
        把 WordBrowser 和 meaningBrowser 更新
        :param index: 第几个数
        :return: None
        """
        # 更新 currentWord
        self.currentWord = self.wordsOAB[self.currentBook][self.currentLesson][index][0]
        self.ui.wordBrowser.setText(self.currentWord)

        if self.wordsOAB[self.currentBook][self.currentLesson][index][1][0] is not None:
            self.ui.meaningBrowser.setText(
                str(self.wordsOAB[self.currentBook][self.currentLesson][index][1][0]) +
                self.wordsOAB[self.currentBook][self.currentLesson][index][1][1]
            )
        else:
            self.ui.meaningBrowser.setText(
                self.wordsOAB[self.currentBook][self.currentLesson][index][1][1]
            )

        # 居中显示
        self.ui.wordBrowser.setAlignment(Qt.AlignCenter)
        self.ui.meaningBrowser.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

    def next(self):
        if len(self.wordsOAB) == 0:
            pass
        elif self.currentIndex < self.lessonLen - 1:
            self.ui.MenuBtn_1.setEnabled(False)
            self.ui.backBtn.setVisible(True)

            # 第一轮要先 index+1 再update
            if self.countRound == 0:
                self.currentIndex += 1
                # self.saveData()
                self.updateWord(self.currentIndex)
                # 更新count
                self.ui.countBrowser_1.setText("  " + str(self.currentIndex + 1))

            # 第二轮 要先update 再加一
            elif self.countRound == 1:
                self.ui.showBtn.setVisible(True)

                self.currentIndex += 1
                if self.currentIndex == 0:
                    self.ui.backBtn.setEnabled(False)
                # 让backButton可以正常使用
                self.ui.backBtn.setEnabled(True)
                self.updateWord(self.currentIndex)
                # 不显示意思
                self.ui.meaningBrowser.setText("")
                # 更新count
                self.ui.countBrowser_1.setText("  " + str(self.currentIndex + 1))

        # 第一轮结束
        elif self.currentIndex == self.lessonLen - 1 and self.countRound == 0:
            self.ui.backBtn.setEnabled(False)

            self.currentIndex = -1  # 设置成-1 就可以先更新变量 再update了
            self.ui.wordBrowser.setText("SecondRound")
            self.ui.meaningBrowser.setText("这回可没有中文意思了哦！\n不过你可以点击show来查看\nAre you Ready?")

            self.countRound = 1

        # 第二轮结束
        elif self.currentIndex == self.lessonLen - 1 and self.countRound == 1:
            # self.currentIndex = 0
            self.ui.showBtn.setVisible(False)
            self.ui.NextBtn.setEnabled(False)
            self.ui.wordBrowser.setText("Take a Quiz")
            self.ui.backBtn.setEnabled(False)
            self.ui.translateBtn.setEnabled(False)
            self.ui.MenuBtn_1.setEnabled(True)
            return

    def back(self):
        self.currentIndex -= 1

        if self.currentIndex == 0:
            self.ui.backBtn.setEnabled(False)
        self.updateWord(self.currentIndex)
        # 更新count
        self.ui.countBrowser_1.setText("  " + str(self.currentIndex + 1))
        # self.saveData()

    def translate(self):
        ProunceList, MeaningList = getTranslationFromYouDao.translate(self.currentWord)
        tmp = "音标:"
        for each in ProunceList:
            tmp += each
        tmp += "\n"
        for each in MeaningList:
            tmp += each + "\n"
        self.ui.meaningBrowser.setText(tmp)


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
