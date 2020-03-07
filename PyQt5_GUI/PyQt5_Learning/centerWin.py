# 需要导入QDesktopWidget来获取窗口和屏幕大小
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow
import sys


class CenterWin(QMainWindow):
    def __init__(self, parent=None):
        super(CenterWin, self).__init__()

        self.setWindowTitle("CenterWinClass")

        self.resize(400, 300)

    def center(self):
        # 获得屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        winGeo = self.geometry()

        # 计算新的右上角坐标
        newLeft = (screen.width() - winGeo.width()) / 2
        newTop = (screen.height() - winGeo.height()) / 2

        # 移动窗口到中心
        self.move(newLeft, newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CenterWin()
    win.show()

    sys.exit(app.exec_())
