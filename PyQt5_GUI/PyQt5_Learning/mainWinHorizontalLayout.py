import sys
import horizontalLayout
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    # 创建实例
    app = QApplication(sys.argv)
    # 创建主窗口
    mainWin = QMainWindow()
    # 创建Ui的实例对象
    ui = horizontalLayout.Ui_MainWindow()
    # 调用ui的方法
    ui.setupUi(mainWin)

    mainWin.show()
    sys.exit(app.exec_())
