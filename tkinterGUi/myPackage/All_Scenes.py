import random
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showwarning, showinfo
from tkinter.ttk import Combobox
import myPackage.functions
import pickle


def main():
    # import sys
    # sys.path.append(r"C:\Users\Armand\Desktop\WordApplication")
    mainloop()


class FirstScene:
    """干什么都别忘了给组件 pack() or grid() or place()"""

    def __init__(self):

        # self.recordList = self.getDate(record)
        # 定义需要用到的参数

        self.pathList = [r"myPackage/vocabularyLib/SatVocabulary.xlsx"]

        # self.pathList = []
        self.lessonNum = 0
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
        self.currentWord = "请选择一种上传方式\n上传或解析本地\n如果需要上传更多文件\n可以通过左上角file->open上传"
        self.currentPOS = "Excel 格式 需为：\n第一列:单词  第二列:词性  第三列:意思"
        self.currentMeaning = "贝塔思英语欢迎您"
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
        # 重置数据
        # self.saveData()

        # 获取数据
        self.getData()

        # 设置root Scene #1
        self.root = Tk()
        self.root.title("RemV Alpha-version")
        # 设定 根窗口size
        self.root.geometry("+500+130")
        # 表示大小由子组件决定
        self.root.grid_propagate(True)
        # alphas 是透明度
        self.root.attributes("-alpha", 0.98)
        # 设置窗口大小不可变
        self.root.resizable(True, True)

        self.menuBar = Menu(self.root, borderwidth=20)
        # 设置File下拉菜单
        self.fileMenu = Menu(self.menuBar, tearoff=False)
        self.fileMenu.add_command(label="open", command=self.openFile)
        self.fileMenu.add_command(label="save", command=self.saveData)
        # menuBar 设置成 Cascading 的状态
        self.menuBar.add_cascade(label="File", menu=self.fileMenu, font="system, 15")
        self.menuBar.add_cascade(label="Contact me", font="system, 15")
        # 链接 菜单 和 root
        self.root.config(menu=self.menuBar)

        # BookLabel
        self.BookLabel = Label(text="Book", font='system, 10', padx=10, pady=10)
        self.BookLabel.grid(row=0, column=0)
        # LessonLabel
        self.LessonLabel = Label(text="Lesson", font="system, 10", padx=20, pady=10)
        self.LessonLabel.grid(row=0, column=1)
        # SequenceLabel
        self.SeqLabel = Label(text="Sequence", font="system, 10", padx=20, pady=10)
        self.SeqLabel.grid(row=0, column=2)

        # ComboBox for Book
        self.bookCombo = Combobox(self.root, values=["请选择", "上传文件", "点我解析已有excel"], state="readonly", width=15)
        self.bookCombo.current(0)
        self.bookCombo.grid(row=1, column=0, padx=15, sticky=W)
        self.bookCombo.bind("<<ComboboxSelected>>", self.callbackFuncForBook)
        # self.bookCombo.bind(('<Configure>', self.changeWidth))

        # ComboBox for Lesson
        self.lessonCombo = Combobox(self.root, values=self.lessonList, state="readonly", width=15)
        self.lessonCombo.grid(row=1, column=1, padx=15, sticky=W)
        self.lessonCombo.bind("<<ComboboxSelected>>", self.callbackFuncForLesson)

        # ComboBox for SeqCombo
        self.seqCombo = Combobox(self.root, values=["List Order", "Random (未开发)"], state="readonly", width=15)
        self.seqCombo.current(0)
        self.seqCombo.grid(row=1, column=2, padx=15, sticky=W)
        self.seqCombo.bind("<<ComboboxSelected>>", self.callbackFuncForSeq)
        self.seqCombo['state'] = 'disabled'

        # LabelFrame
        self.separatorVar = StringVar()
        self.separatorVar.set("共学习 %d  次, 本次共学习 %d  个单词。 累积学习 %d  个单词。\n上次进度: %s" % (
            self.totalStudyTime, self.nowNum, self.accumulativeNum, self.lastProgress))
        self.labelSeparator = Label(self.root, textvariable=self.separatorVar, fg='blue',
                                    justify=CENTER)
        self.labelSeparator.grid(row=2, column=0, columnspan=4)
        # 设置第二行最小高度
        self.root.grid_rowconfigure(2, minsize=70)

        # LabelFrame for words
        # LabelFrame 继承的时候要设置大小 不然默认为0
        self.wordLabelFrame = LabelFrame(self.root, text='未读取文件', bg='#ebebeb',
                                         fg="#4da6ff", width=450, height=50)
        self.wordLabelFrame.grid(row=3, column=0, columnspan=4, sticky=W, padx=15)
        self.root.grid_rowconfigure(3, minsize=70)

        # LabelFrame for Part of speech
        self.POSLabelFrame = LabelFrame(self.root, text="@author: Armand", bg='#ebebeb',
                                        fg="#4da6ff", width=500, height=70)
        self.POSLabelFrame.grid(row=4, column=0, columnspan=4, sticky=W, padx=15, pady=10)
        self.root.grid_rowconfigure(4, minsize=70)

        # LabelFrame for Meanings
        self.MeaningLabelFrame = LabelFrame(self.root, text="别让英语成为负担", bg='#ebebeb',
                                            fg="#4da6ff", width=450, height=70)
        self.MeaningLabelFrame.grid(row=5, column=0, columnspan=4, sticky=W, padx=15, pady=5)
        self.root.grid_rowconfigure(5, minsize=70)

        # Content for words
        self.wordVariable = StringVar()
        self.wordVariable.set(self.currentWord)
        self.wordLabel = Label(self.wordLabelFrame, textvariable=self.wordVariable, font="7", width=25)
        self.wordLabel.grid(columnspan=4, sticky=W)

        # Message for Part of Speech
        self.POSVariable = StringVar()
        if self.currentPOS is None:
            self.POSVariable.set("")  # 更新内容框的内容
        else:
            self.POSVariable.set(self.currentPOS)  # 更新内容框的内容
        self.POSLabel = Label(self.POSLabelFrame, textvariable=self.POSVariable, font="7", width=40)
        self.POSLabel.grid(columnspan=4, sticky=W)

        # Message for Meanings
        self.meaningVariable = StringVar()
        self.meaningVariable.set(self.currentMeaning)
        self.meaningLabel = Label(self.MeaningLabelFrame, textvariable=self.meaningVariable, font="7", width=25)
        self.meaningLabel.grid(columnspan=4, sticky=W)

        # Frame for Button Frame on Top Position
        self.ButtonFrameTop = Frame(self.root, width=140, height=100)
        self.ButtonFrameTop.grid(row=3, column=2, columnspan=2)

        # Frame for Button Frame on Bottom Position
        self.ButtonFrameBottom = Frame(self.root, width=140, height=100)
        self.ButtonFrameBottom.grid(row=5, column=2, columnspan=2)

        # Test Button
        # command 里面不能带参数和括号 否则要加上lambda：
        self.testButton = Button(self.ButtonFrameTop, text="Test", width=10, height=4, bg="#fce5cd", fg="black",
                                 font="15",
                                 command=self.Test)
        self.testButton.grid()
        self.testButton.grid_forget()

        # NextButton
        self.nextButton = Button(self.ButtonFrameTop, text="Next", width=10, height=1, bg="#ffe599",
                                 font="system,20", command=self.nextWord)
        self.nextButton.grid(row=0, column=0, pady=5)
        self.nextButton.grid_forget()
        self.root.bind("<KeyPress-Return>", self.enterPress)
        self.root.bind("<KeyRelease-Return>", self.enterRelease)
        # BackButton
        self.backButton = Button(self.ButtonFrameTop, text="Back", width=10, height=1, bg="#f4cccc", font="20",
                                 cursor="arrow", command=self.backWord)
        self.backButton.grid(row=1, column=0, pady=5)
        self.backButton.grid_forget()

        # Translate Button
        self.translateVar = StringVar()
        self.translateVar.set("在线翻译")
        self.translateButton = Button(self.ButtonFrameBottom, textvariable=self.translateVar, width=10, height=1,
                                      bg="#cfe2f3",
                                      font="system,20", command=self.translate)
        self.translateButton.grid(row=0, column=0, pady=5)
        self.translateButton.grid_forget()

        # show Button
        self.showButton = Button(self.ButtonFrameBottom, text="Show Me", width=10, height=1, bg="#cfe2f3",
                                 font="system,20", command=self.translate)
        self.showButton.grid(row=0, column=0, pady=5)
        self.showButton.grid_forget()

        # 爬虫标语
        self.labelWebSpider = Label(self.root,
                                    text="- - - - - - - - - - - All translation results are gotten from YOUDAO - - - - - - - - - - -",
                                    fg='blue',
                                    font="system, 10", justify=CENTER)
        self.labelWebSpider.grid(row=6, column=0, columnspan=4, pady=5)
        # 设置第二行最小高度
        self.root.grid_rowconfigure(6, minsize=40)

        # Copyright 标语
        self.labelAuthor = Label(self.root, text="@author 肖凌奥", fg='black', font="system, 8",
                                 justify=LEFT)
        self.labelAuthor.grid(row=7, column=1, columnspan=3, rowspan=3, pady=5, sticky=E)
        # 设置第二行最小高度

        # 图片
        self.pic = PhotoImage(file=r"myPackage/image/menhera.png")
        self.picLabelBottom = Label(self.root, image=self.pic)
        self.picLabelBottom.grid(sticky=SW, row=7, column=0, columnspan=3)

        self.pic2 = PhotoImage(file=r"myPackage/image/menhera-3.png")
        self.picLabelTop = Label(self.ButtonFrameTop, image=self.pic2)
        self.picLabelTop.grid()

        # self.menuBar.bind('<B1-Motion>', self.movewindow)
        # Top Level
        self.TestScene = Toplevel(self.root)
        self.TestScene.withdraw()

        self.labelTopVar = StringVar()
        self.labelTop = Label(self.TestScene, width=60, height=2, bg="#e6ffcc", textvariable=self.labelTopVar,
                              font="10", justify=CENTER)
        self.leftPaneWin = PanedWindow(self.TestScene, height=350, width=self.labelTop.winfo_reqwidth() / 4,
                                       sashrelief="groove")

        self.remain = 20
        self.remainVar = StringVar()
        self.labelRemain = Label(self.leftPaneWin, textvariable=self.remainVar, pady=10, font="10", relief='groove')
        self.rightPaneWin = PanedWindow(self.TestScene, height=350, width=self.labelTop.winfo_reqwidth() / 4 * 3,
                                        bg='white')
        self.MeaningLabelFrameTest = LabelFrame(self.rightPaneWin, text="单词中文意思", bg='white',
                                                fg="#4da6ff")
        self.POSLabelFrameTest = LabelFrame(self.rightPaneWin, text="Part of Speech", bg='white',
                                            fg="#4da6ff")
        self.HintLabel = LabelFrame(self.rightPaneWin, text='Hint', bg='white',
                                    fg="#4da6ff")
        self.hintVariable = StringVar()
        self.hintLabel = Label(self.HintLabel, textvariable=self.hintVariable, font="7", width=25)
        self.POSVariableTest = StringVar()
        self.POSLabelTest = Label(self.POSLabelFrameTest, textvariable=self.POSVariableTest, font="7")
        self.meaningVariableTest = StringVar()
        self.meaningLabelTest = Label(self.MeaningLabelFrameTest, textvariable=self.meaningVariableTest, font="7",
                                      width=25)
        self.meaningEntry = Entry(self.rightPaneWin, width=20, font="20", justify=CENTER,
                                  highlightcolor='#D8BFD8', highlightthickness=1, bg="#FDF5E6")

        # Testscene 右边的单词添加表
        self.tasks = []
        self.countTask = 0

        self.colorAlter = 1
        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

        # 第一次使用时的欢迎和介绍
        if self.totalStudyTime == 0:
            self.intro = showinfo("软件介绍和说明", "致用户的一封信：\n\t欢迎使用RemV,"
                                             "这是一款可以帮助你深度记忆单词的一款软件。\n\t"
                                             "使用说明：1.上传文件或者解析本地的库。（上传过一次\n\t\t  就不用上传第二次了！)"
                                             "\n\t2. 选择一个Lesson。\n\t3. 点击\"next\"按钮开始你的背单词之旅~\n\t祝你好运~逢考必过~让英语不再是负担！\n\t"
                                             "界面灵感来源于 Anki 2.0\n\n肖凌奥 "
                                             "Armand\n联系方式(微信): xla920338028")

    def moveWindow(self, event):
        print(event.x, event.y)
        self.root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

    # 用 dialog widget 打开文件
    def openFile(self):
        path = r""
        path += filedialog.askopenfilename(defaultextension=".xlsx", filetypes=[("XLSX", ".xlsx")], title="打开文件哦，亲~")
        if path == "":
            return

        self.pathList.append(path)
        for i in self.pathList:
            # print(i) 调试
            if i != path:
                self.pathList.append(path)
                self.parseFile(path)
            else:
                self.parseFile(i)

    def parseFile(self, path):
        # 处理 bookCombo
        tmpList1 = []
        tmpList1 += myPackage.functions.getBookNames(self.pathList)

        self.bookCombo["values"] = tmpList1
        self.bookCombo.current(newindex=len(self.bookCombo["values"]) - 1)
        # self.currentBook = tmpList[len(self.bookCombo["values"]) - 1]

        # 处理lessonCombo
        tmpList2 = myPackage.functions.excelParse(path)
        self.lessonNum = myPackage.functions.getLessonNum(tmpList2)
        self.setLessons(self.lessonNum)

        # 处理words 把SAT单词书 分成好几节课 然后把SAT这真本书 放到wordsOAB 里面 名字与书的内容
        self.wordsLFSB = (myPackage.functions.divideIntoLessons(myPackage.functions.excelParse(path)))
        self.wordsOAB.update({tmpList1[len(self.bookCombo["values"]) - 1]: self.wordsLFSB})
        self.currentBook = tmpList1[len(self.bookCombo["values"]) - 1]

        self.updateAll()
        self.wordLabelFrame['text'] = "这是Lesson %s 的第  %d  个单词" % (self.currentLesson, self.currentIndex)
        self.POSLabelFrame['text'] = "词性"
        self.MeaningLabelFrame['text'] = "翻译 or 意思"
        # 保存数据
        self.saveData()

    def solveGivenPath(self):
        for eachPath in self.pathList:
            self.parseFile(eachPath)

    def setLessons(self, num):
        # 每次都需要初始化 lessonList 不然换书的时候就崩了
        self.lessonList = []
        self.lessonList.append("Choose a lesson")
        for i in range(1, num + 1):
            self.lessonList.append("Lesson " + str(i))
        self.lessonCombo["value"] = self.lessonList
        # 默认显示第一节课
        self.lessonCombo.current(0)
        # currentLesson 默认为第一节课 -> 只取最后的数字
        self.currentLesson = 0

    def updateWord(self):
        if self.currentLesson is 0:
            pass
        else:
            # 设置currentWordContent
            self.currentWord = self.wordsOAB[self.currentBook][self.currentLesson - 1][self.currentIndex][0]
            self.wordVariable.set(self.currentWord)  # 更新内容框的内容

    def updatePOS(self):
        if self.currentLesson is 0:
            pass
        else:
            # 设置currentPOSContent
            self.currentPOS = self.wordsOAB[self.currentBook][self.currentLesson - 1][self.currentIndex][1][0]
            if self.currentPOS is None:
                self.POSVariable.set("")  # 更新内容框的内容
            else:
                self.POSVariable.set(self.currentPOS)  # 更新内容框的内容

    def updateMeaning(self):
        if self.currentLesson is 0:
            pass
        else:
            # 设置currentPOSContent
            self.currentMeaning = self.wordsOAB[self.currentBook][self.currentLesson - 1][self.currentIndex][1][1]
            # 解决 _tkinter.TclError: character U+1f62e is above the range (U+0000-U+FFFF) allowed by Tcl 问题
            char_list = [self.currentMeaning[j] for j in range(len(self.currentMeaning)) if
                         ord(self.currentMeaning[j]) in range(65536)]
            self.currentMeaning = ''
            for j in char_list:
                self.currentMeaning = self.currentMeaning + j

            self.meaningVariable.set(self.currentMeaning)  # 更新内容框的内容

    # 内容全部更新
    def updateAll(self):
        self.updateWord()
        self.updatePOS()
        self.updateMeaning()

    # 保存文件
    def saveData(self):
        # 第一个数据：pathList
        # 第二个数据：accumulativeNum
        # 第三个数据：totalStudyTime
        # 第四个数据：上次进度
        try:
            with open('myData.pickle', 'wb') as handle:
                pickle.dump(self.pathList, handle, protocol=pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.accumulativeNum, handle, protocol=pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.totalStudyTime, handle, protocol=pickle.HIGHEST_PROTOCOL)
                if self.totalStudyTime == 0:
                    self.lastProgress = "欢迎使用这个软件，希望你可以喜欢"
                else:
                    self.lastProgress = "%s 的 Lesson %d 的第 %d 个单词" % (
                        self.currentBook, self.currentLesson, self.currentIndex)
                    pickle.dump(self.lastProgress, handle, protocol=pickle.HIGHEST_PROTOCOL)
        except:
            pass

    def getData(self):
        try:
            with open('myData.pickle', 'rb') as handle:
                self.pathList = pickle.load(handle)
                self.accumulativeNum = pickle.load(handle)
                self.totalStudyTime = pickle.load(handle)
                try:
                    self.lastProgress = pickle.load(handle)
                except:
                    pass
        except:
            pass

    def callbackFuncForBook(self, event):
        # Python 的 == 是匹配字符串  is 是地址
        if self.bookCombo.get() == "点我解析已有excel":
            if len(self.pathList) == 0:
                tmp = showwarning(title="错误提示", message="未找到本地文件，请上传")
            self.solveGivenPath()
        elif self.bookCombo.get() == "请选择" or self.bookCombo.get() == "":
            pass
        elif self.bookCombo.get() == "上传文件":
            self.openFile()
        else:
            self.currentBook = self.bookCombo.get()
            # print(self.wordsOAB[self.currentBook])
            # 储存的就是 分lesson的单词列表了
            self.lessonNum = len(self.wordsOAB[self.currentBook])
            # print(self.lessonNum)
            self.setLessons(self.lessonNum)

    def callbackFuncForLesson(self, event):
        num = re.compile(r"\d+")
        strTmp = num.search(self.lessonCombo.get())
        self.currentLesson = int(strTmp.group())
        # 更新labelFrame
        self.wordLabelFrame['text'] = "这是Lesson %s 的第  %d  个单词" % (self.currentLesson, self.currentIndex + 1)

        if self.lessonCombo.get()[-1] is not "n":
            self.picLabelTop.grid_forget()
            self.nextButton.grid()
            self.translateButton.grid()
        # 查找这节课的长度
        self.lessonLen = len(self.wordsOAB[self.currentBook][self.currentLesson - 1])
        # 更新
        self.updateAll()
        # 保存数据
        self.saveData()

    def callbackFuncForSeq(self, event):
        self.currentSeq = self.seqCombo.get()

    # 失败的方法 -> 调节下来combobox的宽度
    # def changeWidth(self, event):
    #     font = tkfont.nametofont(str(event.widget.cget('font')))
    #     width = font.measure(self.currentBook + "0") - event.width
    #     style = ttk.Style()
    #     style.configure('TCombobox', postoffset=(0, 0, width, 0))

    # next button function
    def nextWord(self):
        if len(self.wordsOAB) == 0:
            pass
        elif self.currentIndex < self.lessonLen - 1:

            # Combobox 不可交互
            self.lessonCombo['state'] = 'disabled'
            self.bookCombo['state'] = 'disabled'
            self.seqCombo['state'] = 'disabled'
            # 显示 back button
            self.backButton.grid()

            # 第一轮要先 index+1 再update
            if self.countRound == 0:
                self.translateButton.grid()
                self.currentIndex += 1
                self.updateAll()
                self.saveData()

            # 第二轮 要先update 再加一
            elif self.countRound == 1:
                self.currentIndex += 1
                if self.currentIndex == 0:
                    self.backButton.grid_forget()
                self.updateAll()
                self.showButton.grid()
                self.translateButton.grid_forget()
                # 不显示意思
                self.meaningVariable.set("")

            self.separatorVar.set("共学习 %d  次, 本次共学习 %d  个单词。 累积学习 %d  个单词。" % (
                self.totalStudyTime, self.nowNum, self.accumulativeNum))

        elif self.currentIndex == self.lessonLen - 1 and self.countRound == 0:
            self.backButton.grid_forget()
            self.translateButton.grid_forget()

            self.currentIndex = -1  # 设置成-1 就可以先更新变量 再update了
            self.wordVariable.set("下一轮的词将不再显示意思\n不过你同样可以通过\nshow button来查看意思")
            self.POSVariable.set("看看你是否真的掌握了...")
            self.meaningVariable.set("准备好了么？\n 准备好了就开始吧！")
            self.countRound = 1

        elif self.currentIndex == self.lessonLen - 1 and self.countRound == 1:
            # self.currentIndex = 0
            self.wordVariable.set("下个环节将是单词测试环节\n检测你是否掌握了单词的拼写")
            self.POSVariable.set("前后的空格将不会影响单词判读\nGood Luck")
            self.meaningVariable.set("准备好了么？来测试一下吧!")
            self.nextButton.grid_forget()
            # 虽然点不到 但是回车依旧可以触发
            self.root.unbind("<KeyPress-Return>")
            self.root.unbind("<KeyRelease-Return>")

            # 设置label
            self.wordLabelFrame['text'] = "想不想测试一下自己？"
            self.POSLabelFrame['text'] = "测试一下拼写,帮助你更好地记住单词"
            self.MeaningLabelFrame['text'] = "加油，这是最后一步了！"

            self.backButton.grid_forget()
            self.showButton.grid_forget()
            self.testButton.grid()
            return

        self.separatorVar.set("共学习 %d  次, 本次共学习 %d  个单词。 累积学习 %d  个单词。" % (
            self.totalStudyTime, self.nowNum, self.accumulativeNum))

        if self.currentIndex == self.lessonLen - 1 and self.countRound == 1:
            pass
        else:
            self.wordLabelFrame['text'] = "这是Lesson %s 的第  %d  个单词" % (self.currentLesson, self.currentIndex + 1)

    def backWord(self):
        self.currentIndex -= 1

        if self.currentIndex == 0:
            self.backButton.grid_forget()
        self.updateAll()
        if self.countRound == 1:
            self.meaningVariable.set("")
        self.saveData()

    def translate(self):
        if self.controlTranslate:
            self.meaningVariable.set(myPackage.functions.translator(self.currentWord))
            self.controlTranslate = False
            self.translateVar.set("取消翻译")
        else:
            self.updateMeaning()
            self.controlTranslate = True
            self.translateVar.set("在线翻译")

    def show(self):
        self.updateMeaning()

    def enterPress(self, event):
        self.nextButton["relief"] = "sunken"
        self.nextWord()

    def enterRelease(self, event):
        self.nextButton["relief"] = "raised"

    def Test(self):

        self.currentIndex = random.randint(0, 19)

        self.updateAll()
        self.root.withdraw()
        self.TestScene.deiconify()

        self.TestScene.title("Test Scene")
        # 设定 根窗口size
        self.TestScene.geometry("+390+130")
        self.TestScene.grid_propagate(True)
        # alphas 是透明度
        self.TestScene.attributes("-alpha", 0.98)
        # 设置窗口大小不可变
        self.TestScene.resizable(True, True)

        self.labelTopVar.set(self.lastProgress[0:len(self.lastProgress) - 9])

        self.labelTop.grid(row=0, column=0, sticky=N, columnspan=2)

        self.leftPaneWin.pack_propagate(False)
        self.leftPaneWin.grid(row=1, column=0, sticky=W)
        self.leftPaneWin["sashrelief"] = "sunken"

        self.remainVar.set("Remain: %d" % self.remain)
        self.labelRemain.pack(fill=X)

        self.rightPaneWin.grid(row=1, column=1, sticky=W)
        self.rightPaneWin.pack_propagate(False)

        # LabelFrame for Meanings
        self.MeaningLabelFrameTest.place(width=200, height=200, relx=0.08, rely=0.05)

        # LabelFrame for Part of speech
        self.POSLabelFrameTest.place(width=170, height=90, relx=0.53, rely=0.05)

        self.HintLabel.place(width=170, height=90, relx=0.53, rely=0.36)

        # Content for words
        self.hintVariable.set(self.covertTohint())
        self.hintLabel.pack()

        # Message for Part of Speech
        self.POSVariableTest.set(self.currentPOS)
        self.POSLabelTest.pack()

        # Message for Meanings
        self.meaningVariableTest.set(self.currentMeaning)
        self.meaningLabelTest.pack()

        # Entry
        self.meaningEntry.place(width=400, height=70, relx=0.08, rely=0.7)
        self.meaningEntry.focus_set()
        self.meaningEntry.bind("<KeyPress-Return>", self.enterCheck)
        self.meaningEntry.bind("<Key>", self.updateHint)

    def nextRandWord(self):
        if self.noWrongTime:
            self.randomSet.add(self.currentIndex)
            self.nowNum += 1
            self.accumulativeNum += 1
            self.remain -= 1
            self.saveData()
        else:
            self.noWrongTime = True

        if len(self.randomSet) == 20:
            # 结束 Test scene
            self.root.deiconify()
            # 其实还需要判断 currentLesson 有没有越界
            self.currentLesson += 1

            self.currentIndex = 0
            self.lessonCombo.current(self.currentLesson)
            self.updateAll()
            # 更新界面
            self.showButton.grid()
            self.translateButton.grid()
            self.testButton.grid_forget()
            self.TestScene.withdraw()
            self.randomSet = set()
            self.nextButton.grid()
            self.showButton.grid_forget()
            self.countRound = 0

            self.lessonCombo['state'] = 'normal'
            self.bookCombo['state'] = 'normal'
            # 未开放这个选项
            # self.seqCombo['state'] = 'normal'
            self.getData()
            self.separatorVar.set("共学习 %d  次, 本次共学习 %d  个单词。 累积学习 %d  个单词。\n上次进度: %s" % (
                self.totalStudyTime, self.nowNum, self.accumulativeNum, self.lastProgress))
            self.root.bind("<KeyPress-Return>", self.enterPress)
            self.root.bind("<KeyRelease-Return>", self.enterRelease)
            self.nextButton["relief"] = "raised"

            # 清空list里所有组件的pack
            self.removeTask()
            for item in self.tasks:
                item.pack_forget()
            self.tasks = []
            self.remain = 20
            # 更新所有数据
            self.updateAll()
            self.saveData()

            return

        tmp = random.randint(0, 19)
        while tmp in self.randomSet:
            tmp = random.randint(0, 19)
        self.currentIndex = tmp
        self.updateAll()
        self.updateAllTest()

        tmp = random.randint(0, 19)
        while tmp in self.randomSet:
            tmp = random.randint(0, 19)
        self.currentIndex = tmp
        self.updateAll()
        self.updateAllTest()

    def enterCheck(self, event):
        if self.meaningEntry.get().strip() == self.currentWord:
            # 对的话才让下一个词
            self.nextRandWord()
            self.add_task()
            self.removeTask()
        else:
            # 错的话 就知道输入正确为止
            self.hintVariable.set(self.currentWord)
            self.noWrongTime = False
        # 清空 Entry
        self.meaningEntry.delete(0, 'end')

    def updateAllTest(self):
        self.remainVar.set(self.remain)

        self.POSVariableTest.set(self.currentPOS)
        self.meaningVariableTest.set(self.currentMeaning)
        self.hintVariable.set(self.covertTohint())

    def covertTohint(self):
        tmp = self.currentWord[0:1]
        pattern = re.compile(r"[a-z][A-Z]*")
        tmp += pattern.sub("*", self.currentWord[1:])
        return tmp

    def updateHint(self, event):
        self.hintVariable.set(self.covertTohint())

    def add_task(self):
        task_text = self.meaningEntry.get().strip()

        if len(task_text) > 0:
            new_task = Label(self.leftPaneWin, text=task_text, pady=10, font="10")
            if len(self.tasks) < 5:
                _, task_style_choice = divmod(len(self.tasks), 2)
            else:
                _, task_style_choice = divmod(len(self.tasks) + self.colorAlter, 2)
            self.colorAlter += 1
            my_scheme_choice = self.colour_schemes[task_style_choice]

            new_task.configure(bg=my_scheme_choice["bg"])
            new_task.configure(fg=my_scheme_choice["fg"])

            new_task.pack(side=TOP, fill=X)

            self.tasks.append(new_task)

    def removeTask(self):
        if len(self.tasks) > 5:
            task = self.tasks[0]
            # task.master.destroy()
            task.pack_forget()
            self.tasks.pop(0)
