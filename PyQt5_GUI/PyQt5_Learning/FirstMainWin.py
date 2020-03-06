import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class FirstMainWin(QMainWindow):
    # self 就说 QMainWin
    def __init__(self, parent=None):
        super(FirstMainWin, self).__init__(parent)

        # 设置窗口标题
        self.setWindowTitle("这是第一个窗口程序")

        # 设置窗口尺寸
        self.resize(400, 300)

        # 获得状态栏
        self.status = self.statusBar()
        # 设置状态栏的内容和存在时长 时间单位是毫秒(ms) 5000ms = 5s
        self.status.showMessage("状态消息内容", 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 设置应用图标 后缀名是 ico
    # app.setWindowIcon(QIcon("path"))

    # 创建类实例
    mainWin = FirstMainWin()
    mainWin.show()

    sys.exit(app.exec_())
