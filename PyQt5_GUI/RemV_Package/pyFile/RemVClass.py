import os
import pickle
import sys
from random import randint
import re

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QPalette, QBrush, QCursor
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from pyFile import FirstGui_ChineseVersion, functions, getTranslationFromYouDao


# def resource_path(relative_path):
#     """
#     定义一个读取相对路径的函数
#       """
#     if hasattr(sys, "_MEIPASS"):
#         base_path = sys._MEIPASS
#     else:
#         base_path = os.path.abspath(".")
#     return os.path.join(base_path, relative_path)

def toRelativePath(path):
    nowPath = os.getcwd()
    newPath = os.path.join(nowPath, path)
    return newPath

def loadQss():

    with open(toRelativePath(r"lib/qss.txt"), "r") as f:
        return f.read()


class RemVClass(QMainWindow):
    def __init__(self):
        super().__init__()
        # 英文版
        # self.ui = FirstGui.Ui_MainWindow()
        # FirstGui.Ui_MainWindow.setupUi(self.ui, self)

        # 中文版
        self.ui = FirstGui_ChineseVersion.Ui_MainWindow()
        FirstGui_ChineseVersion.Ui_MainWindow.setupUi(self.ui, self)

        # 紧张窗口缩放和拉伸
        self.setWindowFlag(Qt.FramelessWindowHint)

        # 更改图片尺寸
        self.image = QPixmap(toRelativePath(r"lib/res/image/background_3"))
        self.image = self.image.scaled(1259, 878, Qt.IgnoreAspectRatio, Qt.FastTransformation)

        # titleBar 图片
        self.titleImage = QPixmap(toRelativePath(r"lib/res/image/background_5"))
        self.titleImage = self.titleImage.scaled(1257, 25, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.ui.TitleBar_Label.setPixmap(self.titleImage)

        # 添加主窗口背景图
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap(self.image)))
        self.setPalette(palette)

        # 先disable
        self.ui.stackedWidget.setEnabled(False)
        # self.ui.stackedWidget.setCurrentIndex(3)

        # 给各个按钮加对应图标
        self.ui.uploadButton.setIcon(QIcon(toRelativePath(r"./lib/res/image/upload.png")))
        self.ui.MemorizeBtn_0.setIcon(QIcon(toRelativePath(r"./lib/res/image/brain.png")))
        self.ui.MenuBtn_1.setIcon(QIcon(toRelativePath(r"./lib/res/image/home_2.png")))
        self.ui.MenuBtn_2.setIcon(QIcon(toRelativePath(r"./lib/res/image/home_2.png")))
        self.ui.QuizBtn_0.setIcon(QIcon(toRelativePath(r"./lib/res/image/quiz.png")))
        self.ui.QuizBtn_1.setIcon(QIcon(toRelativePath(r"./lib/res/image/quiz.png")))
        self.ui.helpBtn.setIcon(QIcon(toRelativePath(r"./lib/res/image/question.png")))
        self.ui.translateBtn.setIcon(QIcon(toRelativePath(r"../lib/res/image/translate.png")))
        self.ui.backBtn.setIcon(QIcon(toRelativePath(r"./lib/res/image/back_2.png")))
        self.ui.NextBtn.setIcon(QIcon(toRelativePath(r"./lib/res/image/next_2.png")))
        self.ui.showBtn.setIcon(QIcon(toRelativePath(r"./lib/res/image/word.png")))
        self.ui.statusBtn.setIcon(QIcon(toRelativePath(r"./lib/res/image/wrong.png")))
        self.ui.exitBtn.setIcon(QIcon(toRelativePath(r"./lib/res/image/exit.png")))

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

        # 给 memorize, quiz, menu 添加事件 切屏事件
        self.ui.MenuBtn_1.clicked.connect(self.changeScene_0)
        self.ui.MenuBtn_2.clicked.connect(self.changeScene_0)
        self.ui.MemorizeBtn_0.clicked.connect(self.changeScene_1)
        self.ui.QuizBtn_0.clicked.connect(self.changeScene_2)
        self.ui.QuizBtn_1.clicked.connect(self.changeScene_2)

        # next, back, translate, show, exit 添加点击事件
        self.ui.NextBtn.clicked.connect(self.next)
        self.ui.backBtn.clicked.connect(self.back)
        self.ui.translateBtn.clicked.connect(self.translate)
        self.ui.showBtn.clicked.connect(lambda: self.updateWord(self.currentIndex))
        self.ui.exitBtn.clicked.connect(lambda: self.close())

        # QuizScene 事件
        # 回车键叫return
        self.ui.enterEdit.returnPressed.connect(self.enterCheck)
        self.ui.enterEdit.textChanged.connect(self.checkEverySyllable)

        # 初始化数据
        # 保存book路径的list

        self.pathList = [r".\lib\res\word_Repository\SatVocabulary.xlsx"]

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
        self.lastProgress = "欢迎使用这个软件，希望你可以喜欢"
        self.randomSet = set()
        self.noWrongTime = True
        self.remain = 19
        self.showHint = True
        self.firstQuiz = True

        # 获取上次进度
        try:
            self.getData()
        except:
            pass

        self.ui.progressLabel.setText(self.lastProgress)
        # 调用方法
        # 解析已存在的excel
        self.parseAllBooks(self.pathList)

        if self.totalStudyTime == 0:
            QMessageBox.information(self, "介绍和使用说明", "致用户的一封信：\n\n\t欢迎使用RemV,"
                                                     "这是一款可以帮助你深度记忆单词的\n\t一款软件。"
                                                     "此软件通过与用户互动提高注意力,从而达\n\t到更好的记忆效果!\n\n"
                                                     "使用说明：\n\t1.上传文件或者使用本地提供的库。"
                                                     "\n\t2. 选择一个自动生成的Lesson。\n\t3. 点击\"Memorize\"或\" Quiz\"按钮 \n\n\t"
                                                     "不再让英语成为负担, 祝你好运!\n\n肖凌奥 "
                                                     "Armand\n联系方式(微信): xla920338028")

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
        self.ui.stackedWidget.setCurrentIndex(0)
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
        # 在测试完后 更新label
        self.ui.progressLabel.setText(self.lastProgress)

        # enable
        self.ui.translateBtn.setEnabled(True)
        self.ui.NextBtn.setEnabled(True)
        # 初始化第二轮的值
        self.currentIndex = 0
        self.countRound = 0

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
            self.saveData()
        else:
            print("上传动作取消")


    def changeScene_1(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.bookListWidget.setEnabled(False)
        self.ui.lessonListWidget.setEnabled(False)
        self.ui.QuizBtn_1.setVisible(False)

        # 把第一个元素更新
        self.updateWord(0)
        self.ui.countBrowser_1.setText("  1")
        self.ui.backBtn.setEnabled(False)
        self.ui.showBtn.setVisible(False)

    def changeScene_0(self):
        self.setOverViewScene()
        self.ui.stackedWidget.setCurrentIndex(0)

    def changeScene_2(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.enterEdit.setEnabled(True)
        self.nextRandWord()
        self.ui.enterEdit.setFocus()

        self.ui.statusBtn.setVisible(True)
        self.ui.bookListWidget.setEnabled(False)
        self.ui.lessonListWidget.setEnabled(False)
        self.ui.quizLabel.setText(
            "%s Lesson %d Quiz" % (functions.getBookNames([self.currentBook])[0], self.currentLesson + 1))

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
        self.ui.meaningBrowser.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def next(self):
        if len(self.wordsOAB) == 0:
            pass
        elif self.currentIndex < self.lessonLen - 1:
            self.ui.translateBtn.setEnabled(True)
            self.ui.MenuBtn_1.setVisible(False)
            self.ui.backBtn.setEnabled(True)

            # 第一轮要先 index+1 再update
            if self.countRound == 0:
                self.currentIndex += 1
                self.saveData()
                self.updateWord(self.currentIndex)
                # 更新count
                self.ui.countBrowser_1.setText("  " + str(self.currentIndex + 1))

            # 第二轮 要先update 再加一
            elif self.countRound == 1:
                self.ui.showBtn.setVisible(True)

                self.currentIndex += 1
                if self.currentIndex == 0:
                    self.ui.backBtn.setEnabled(False)

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
            self.ui.countBrowser_1.setText("")
            self.countRound = 1
            self.ui.translateBtn.setEnabled(False)

        # 第二轮结束
        elif self.currentIndex == self.lessonLen - 1 and self.countRound == 1:
            # self.currentIndex = 0
            self.ui.showBtn.setVisible(False)
            self.ui.NextBtn.setEnabled(False)
            self.ui.wordBrowser.setText("Take a Quiz")
            self.ui.meaningBrowser.setText("Quiz is the core of this app!")
            self.ui.backBtn.setEnabled(False)
            self.ui.translateBtn.setEnabled(False)
            self.ui.MenuBtn_1.setVisible(True)
            self.ui.QuizBtn_1.setVisible(True)
            return

    def back(self):
        self.currentIndex -= 1

        if self.currentIndex == 0:
            self.ui.backBtn.setEnabled(False)
        # 更新count
        self.ui.countBrowser_1.setText("  " + str(self.currentIndex + 1))
        self.saveData()
        self.updateWord(self.currentIndex)

        if self.countRound == 1:
            self.ui.meaningBrowser.setText("")

    def nextRandWord(self):
        # 不是first time
        if self.noWrongTime and not self.firstQuiz:
            self.ui.wordEnterListWidget.addItem(self.currentWord)
            self.randomSet.add(self.currentIndex)
            self.remain -= 1
            # 是firstTime
            self.nowNum += 1
            self.accumulativeNum += 1
            self.saveData()
        else:
            self.firstQuiz = False
            self.noWrongTime = True

        if len(self.randomSet) == 20:
            # 结束 Test scene
            self.ui.MenuBtn_2.setVisible(True)
            # 其实还需要判断 currentLesson 有没有越界
            self.currentIndex = 0
            self.randomSet = set()
            self.countRound = 0
            # 更新界面
            self.ui.meaningBrowser_2.setText("Back to the Menu, and Start a new lesson!")
            self.ui.remainLabel.setText("Congratulations!")
            self.ui.hintEdit.setText("")
            self.ui.statusBtn.setVisible(False)
            self.ui.enterEdit.setEnabled(False)
            self.ui.MenuBtn_2.setFocus(True)

            # self.getData()
            self.remain = 19
            # 清空list里所有组件的
            self.ui.wordEnterListWidget.clear()

            self.saveData()
            self.getData()

            # self.currentLesson += 1
            return

        tmp = randint(0, 19)
        while tmp in self.randomSet:
            tmp = randint(0, 19)
        self.currentIndex = tmp
        self.currentWord = self.wordsOAB[self.currentBook][self.currentLesson][self.currentIndex][0]
        self.currentMeaning = self.wordsOAB[self.currentBook][self.currentLesson][self.currentIndex][1][1]
        # self.updateAll()
        self.updateAllTest()

    def updateAllTest(self):
        self.ui.meaningBrowser_2.setText(self.currentMeaning)
        self.ui.hintEdit.setText(self.convertTohint())
        self.ui.remainLabel.setText("Remain: %s" % str(self.remain + 1))
        self.ui.meaningBrowser_2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def convertTohint(self):
        tmp = self.currentWord[0:1]
        pattern = re.compile(r"[a-z][A-Z]*")
        tmp += pattern.sub("*", self.currentWord[1:])
        return tmp

    def enterCheck(self):
        self.ui.MenuBtn_2.setVisible(False)
        if self.ui.enterEdit.text().strip() == self.currentWord:
            # 对的话才让下一个词
            self.nextRandWord()
        else:
            # 错的话 就知道输入正确为止
            self.ui.hintEdit.setText(self.currentWord)
            self.noWrongTime = False
            self.showHint = False
        # 清空 Entry
        self.ui.enterEdit.clear()

    def checkEverySyllable(self):
        # 一有输入就消除提示 检查上次有没有输错
        if self.showHint:
            self.ui.hintEdit.setText(self.convertTohint())
        else:
            self.showHint = True

        if self.ui.enterEdit.text().strip() == self.currentWord:
            self.ui.statusBtn.setIcon(QIcon(toRelativePath(r"./lib/res/image/correct.png")))
        else:
            self.ui.statusBtn.setIcon(QIcon(toRelativePath(r"./lib/res/image/wrong.png")))

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
            # 记得转换成相对路径
            self.parseFile(toRelativePath(each))

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

        # 保存数据
        self.saveData()

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

    # 保存文件
    def saveData(self):
        # 第一个数据：pathList
        # 第二个数据：accumulativeNum
        # 第三个数据：totalStudyTime
        # 第四个数据：上次进度
        try:
            with open(toRelativePath('./myData.pickle'), 'wb') as handle:
                pickle.dump(self.pathList, handle, protocol=pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.accumulativeNum, handle, protocol=pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.totalStudyTime, handle, protocol=pickle.HIGHEST_PROTOCOL)
                # currentBook 是地址 currentLesson是下标 得加一
                self.lastProgress = "上次进度: %s Lesson %d  共学习: %d 个单词！" % (
                    functions.getBookNames([self.currentBook])[0], self.currentLesson + 1, self.accumulativeNum)
                pickle.dump(self.lastProgress, handle, protocol=pickle.HIGHEST_PROTOCOL)
        except:
            pass

    def getData(self):
        try:
            with open(toRelativePath('./myData.pickle'), 'rb') as handle:
                self.pathList = pickle.load(handle)
                self.accumulativeNum = pickle.load(handle)
                self.totalStudyTime = pickle.load(handle)
                try:
                    self.lastProgress = pickle.load(handle)
                except:
                    pass
        except:
            pass

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True

            self.m_DragPosition = event.globalPos() - self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            # print(event.globalPos())
            # print(event.pos())
            # print(self.pos())
        if event.button() == Qt.RightButton:
            self.close()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            # 当左键移动窗体修改偏移值
            # QPoint
            # 实时计算窗口左上角坐标
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

