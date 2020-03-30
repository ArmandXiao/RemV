from urllib import parse, request
import re

"""
@copyright   Copyright 2020 RemV
@license     GPL-3.0 (http://www.gnu.org/licenses/gpl-3.0.html)
@author      Lingao Xiao 肖凌奥 <920338028@qq.com>
@version     Alpha version
@link        https://github.com/ArmandXiao/RemV.git
"""

def translate(word):
    '''
    Can translate from English to Chinese Only
    :param word: an English word
    :return: two lists. One contains pronounciations of the word. The other gives all meanings gotten from the website.
    '''
    word = word.replace(" ", "%20")
    url = "http://dict.youdao.com/w/" + word + "/#keyfrom=dict2.top"
    res = request.urlopen(url)

    html = res.read().decode("utf-8")
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


if __name__ == '__main__':
    lista, listb = translate("pig")
    print(lista)
    print(listb)
