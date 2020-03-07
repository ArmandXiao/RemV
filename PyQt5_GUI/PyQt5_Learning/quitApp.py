import sys
# Q H box -> Q horizontal Box Layout 水平布局
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton


class QuitApp(QMainWindow):
    def __init__(self, parent=None):
        super(QuitApp, self).__init__(parent)
        # 设置主窗口尺寸
        self.resize(400, 300)

        # 添加按钮
        self.quitButton = QPushButton("退出应用")
        # 绑定按钮和槽(slot)(方法)
        self.quitButton.clicked.connect(self.onClick_Button)

        # 创建水平布局
        self.horLayout = QHBoxLayout()
        self.horLayout.addWidget(self.quitButton)

        # 需要QWidget来存放所有控件
        self.mainFrame = QWidget()
        self.mainFrame.setLayout(self.horLayout)

        # 给主屏幕设置主widget
        self.setCentralWidget(self.mainFrame)

    # 按钮单击事件方法
    def onClick_Button(self):
        # # 获取按钮发射出的 signal 需要 PYQT_SLOT来做装饰
        # sender = self.sender()

        # sender.text() 获取按钮的文本
        print(self.quitButton.text() + " 被按下了")

        # 获取QApplication实例
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QuitApp()
    win.show()

    sys.exit(app.exec_())
