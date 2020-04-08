import os
import threading
import time
import urllib
from urllib import parse, request
import re

"""
@copyright   Copyright 2020 RemV
@license     GPL-3.0 (http://www.gnu.org/licenses/gpl-3.0.html)
@author      Lingao Xiao 肖凌奥 <920338028@qq.com>
@version     version 1.1
@link        https://github.com/ArmandXiao/RemV.git
"""


def getHtml(word):
    url = "https://dict.eudic.net/dicts/en/" + word

    try:
        res = request.urlopen(url)
    except:
        print("搜索失败")
        return

    html = res.read().decode("utf-8")
    return html


def getPicUrl(word):
    word = word.replace(" ", "%20").strip()
    html = getHtml(word)

    picUrl = re.compile("(<img src=\"(.*?)\")((/\s)|(\s*?))(alt=\"[^(二维码)]*?>)")
    list_ = picUrl.findall(html)

    if len(list_) > 0:
        str_ = list_[0][1]
        if ".jpg" not in list_[0][1]:
            str_ += ".jpg"

        if "https" not in list_[0][1]:
            str_ = "https:" + str_
        return str_
    return None


def downloadPicFromOuLu(word):
    t = threading.Timer(5, lambda: quit())
    t.start()

    word = word.replace(" ", "%20").strip()
    url = getPicUrl(word)

    if url is None:
        print("图片地址不存在: " + word)

    path = os.getcwd() + r"\lib\res\pic"
    fileName = word + ".jpg"

    filePath = os.path.join(path, fileName)

    if not os.path.exists(filePath):
        if not os.path.exists(path):
            os.makedirs(path)
        try:
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent',
                                  'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) '
                                  'Presto/2.8.149 Version/11.10')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(url, filePath)
            print("成功: " + word)
        except:
            print("请求连接网络失败: %s\n" % word)


def getTags(word):
    word = word.replace(" ", "%20").strip()
    html = getHtml(word)

    tagFinder = re.compile("(<span class=\"tag\">)(.{1,5})(</span>)")
    try:
        tagList = tagFinder.findall(html)
        resultList = []
        for each in tagList:
            resultList.append(each[1])
    except:
        return None

    return resultList


if __name__ == '__main__':
    print(getPicUrl("harness"))
