import os
import urllib.request

from playsound import playsound

"""
@copyright   Copyright 2020 RemV
@license     GPL-3.0 (http://www.gnu.org/licenses/gpl-3.0.html)
@author      Lingao Xiao 肖凌奥 <920338028@qq.com>
@version     version 1.1
@link        https://github.com/ArmandXiao/RemV.git
"""

def downloadMP3FromYouDao(word, type_):
    word = word.replace(" ", "%20")
    url = "http://dict.youdao.com/dictvoice?type=%d&audio=%s" % (type_, word)
    path = os.getcwd() + r"\lib\res\pron"
    fileName = word + "_" + str(type_) + ".mp3"

    filePath = os.path.join(path, fileName)

    if not os.path.exists(filePath):
        if not os.path.exists(path):
            os.makedirs(path)
        try:
            urllib.request.urlretrieve(url, filePath)
        except:
            sayTipSound()
            return ""
    else:
        print("mp3文件已存在")

    return filePath


def playSound(word, type_):
    path = downloadMP3FromYouDao(word, type_)
    if path != "":
        playsound(path)
        # del
        os.remove(path)


def sayTipSound():
    playsound(r"lib\res\pron\Please%20check%20your%20internet%20connection_0.mp3")


if __name__ == '__main__':
    playSound("perennial", 1)
