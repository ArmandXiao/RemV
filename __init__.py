"""
@author Armand
GUI灵感源自于
https://www.zhihu.com/question/32703639
Anki client

"""
import myPackage.GUI_FirstScene


def main():
    app = GUI_FirstScene.FirstScene()
    app.totalStudyTime += 1
    app.isFirstTime = False
    GUI_FirstScene.main()
