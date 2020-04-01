import os
import urllib.request

from playsound import playsound


def downloadMP3FromYouDao(word, type_):
    word = word.replace(" ", "%20")
    url = "http://dict.youdao.com/dictvoice?type=%d&audio=%s" % (type_, word)
    path = os.getcwd() + r"\lib\res\pron"
    fileName = word + "_" + str(type_) + ".mp3"
    filePath = os.path.join(path, fileName)

    if not os.path.exists(filePath):
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
