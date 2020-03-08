import sys
import horizontalLayout
from PyQt5.QtWidgets import QApplication, QMainWindow


class mainWInHori(QMainWindow):
    def __init__(self):
        super(mainWInHori, self).__init__()
        # 创建ui类实例
        ui = horizontalLayout.Ui_MainWindow()
        # setup UI
        horizontalLayout.Ui_MainWindow.setupUi(ui, self)

        ui.testButton.clicked.connect(self.onClick)

    def onClick(self):
        print("hello")

if __name__ == '__main__':
    # 创建实例
    app = QApplication(sys.argv)
    # 创建主窗口
    mainWin = mainWInHori()

    mainWin.show()
    sys.exit(app.exec_())
