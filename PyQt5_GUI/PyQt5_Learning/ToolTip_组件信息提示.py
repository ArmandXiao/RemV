import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton, QToolTip


class ToolTip(QMainWindow):
    def __init__(self):
        super(ToolTip, self).__init__()
        self.initUI()

    def initUI(self):
        # 用QToolTip类静态方法设置字体
        # 使用QFont自带的字体包
        QToolTip.setFont(QFont('Times New Roman', 7))
        self.setToolTip("This is a window")
        self.resize(300, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ToolTip()
    win.show()

    sys.exit(app.exec_())
