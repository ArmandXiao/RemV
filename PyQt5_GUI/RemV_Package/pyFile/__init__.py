import sys

from PyQt5.QtWidgets import QApplication

from RemVClass import RemV, loadQss


def main():
    app = QApplication(sys.argv)
    win = RemV()
    win.setWindowTitle("RemV - alpha")
    win.setStyleSheet(loadQss())
    win.show()

    win.totalStudyTime += 1
    win.isFirstTime = False

    sys.exit(app.exec_())
