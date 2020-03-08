import sys
import FirstGui
from PyQt5.QtWidgets import QMainWindow, QApplication


def loadQss():
    with open(r"qss.txt", "r") as f:
        return f.read()


class RemV(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = FirstGui.Ui_MainWindow()
        FirstGui.Ui_MainWindow.setupUi(self.ui, self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = RemV()
    win.setStyleSheet(loadQss())
    win.show()

    sys.exit(app.exec_())
