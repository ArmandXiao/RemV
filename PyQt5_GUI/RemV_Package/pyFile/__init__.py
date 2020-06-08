import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from RemVClass import RemVClass, loadQss

"""
@copyright   Copyright 2020 RemV
@license     GPL-3.0 (http://www.gnu.org/licenses/gpl-3.0.html)
@author      Lingao Xiao 肖凌奥 <920338028@qq.com>
@version     version 1.1
@link        https://github.com/ArmandXiao/RemV.git
"""


def main():
    app = QApplication(sys.argv)
    win = RemVClass()

    win.setStyleSheet(loadQss())
    win.show()

    win.totalStudyTime += 1
    win.isFirstTime = False

    sys.exit(app.exec_())
