import sys

from PyQt5.QtWidgets import QApplication
from RemVClass import RemVClass, loadQss


def main():
    app = QApplication(sys.argv)
    win = RemVClass()
    win.setStyleSheet(loadQss())
    win.show()

    win.totalStudyTime += 1
    win.isFirstTime = False

    sys.exit(app.exec_())
