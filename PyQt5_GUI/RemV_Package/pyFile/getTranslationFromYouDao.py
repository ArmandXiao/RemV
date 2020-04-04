import os
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
    word = word.replace(" ", "%20")
    url = "http://dict.youdao.com/w/" + word + "/#keyfrom=dict2.top"

    try:
        res = request.urlopen(url, timeout=3)
    except:
        print("搜索失败")
        return

    html = res.read().decode("utf-8")
    return html


def translate(word):
    '''
    Can translate from English to Chinese Only
    :param word: an English word
    :return: two lists. One contains pronounciations of the word. The other gives all meanings gotten from the website.
    '''

    html = getHtml(word)
    if not html:
        return [], []
    pronounce = re.compile(r"<span class=\"phonetic\">.+?</span>")
    meaning = re.compile(r"<li>[^<>].*?</li>")

    proListraw = pronounce.findall(html)
    meanListraw = meaning.findall(html)

    proList = []
    meanList = []
    # 第一个是英式发音 第二个是美式发音
    for each in proListraw:
        proList.append(re.search(r"[[].+[]]", each).group())

    for each in meanListraw:
        tmp = re.search(r">.+<", each).group()
        meanList.append(tmp[1:len(tmp) - 1])

    return proList, meanList


def getFrequency(word):
    """
    Return the frequency of the word
    :param word: word
    :return: int: the frequency of the word
    """
    html = getHtml(word)
    if not html:
        return -1
    findFre = re.compile("\"star star[123456]?\"")

    if not findFre.search(html):
        return -1

    freListRaw = findFre.search(html).group()

    fre = re.search("[0123456]", freListRaw).group()

    return int(fre)

    return filePath


if __name__ == '__main__':
    # lista, listb = translate("pig")
    # print(lista)
    # print(listb)
    getFrequency("there")
