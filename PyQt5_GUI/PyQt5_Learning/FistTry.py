# PyQt5 必须包含两个类 QApplication 和 QWidget
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 建QApplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口大小 单位都是像素 px
    w.resize(400, 200)
    # 移动窗口左上角坐标 -> 调整窗口创建出来的位置
    w.move(300, 300)
    # 设置窗口标题
    w.setWindowTitle("第一个应用")
    # 显示窗口
    w.show()

    # 进入PyQt程序的主循环 保存组件更新 和 不会退出
    # 并通过 exit函数确保程序安全退出 释放资源
    sys.exit(app.exec_())