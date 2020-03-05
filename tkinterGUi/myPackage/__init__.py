"""
@author Armand
GUI灵感源自于
https://www.zhihu.com/question/32703639
Anki client

"""
import myPackage.All_Scenes


def main():
    app = All_Scenes.FirstScene()
    app.totalStudyTime += 1
    app.isFirstTime = False
    All_Scenes.main()
