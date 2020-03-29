import sys

from PyQt5.QtWidgets import QApplication
import RemVClass


def main():
    app = QApplication(sys.argv)
    win = RemVClass.RemVClass()
    win.setStyleSheet(RemVClass.loadQss())
    win.show()

    win.totalStudyTime += 1
    win.isFirstTime = False

    sys.exit(app.exec_())

