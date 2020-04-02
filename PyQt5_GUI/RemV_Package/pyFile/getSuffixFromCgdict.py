from urllib import parse, request
import re
import time
"""
@copyright   Copyright 2020 RemV
@license     GPL-3.0 (http://www.gnu.org/licenses/gpl-3.0.html)
@author      Lingao Xiao 肖凌奥 <920338028@qq.com>
@version     Alpha version
@link        https://github.com/ArmandXiao/RemV.git
"""


def getHtml(word):

    url = "http://www.cgdict.com/index.php?app=cigen&ac=word&w=" + word

    try:
        res = request.urlopen(url, timeout=3)
    except:
        print("搜索失败")
        return

    html = res.read().decode("utf-8")
    return html


def getPreOrSuf(word):
    """
    获取词根词缀
    :param word: An English word
    :return: a string of prefix and a string of a suffix
    """
    if " " in word:
        return "", ""
    html = getHtml(word)
    if not html:
        return "", ""

    getPre = re.compile("(<h3 class=\"pron\">[^(src&)].*?</h3>)([\s\S]*?)(<h3>[^(divclas)].*?</h3>)")
    list_ = getPre.findall(html)

    listPre = []
    listSux = []

    for each in list_:
        for item in each:
            if "词根" in item:
                listSux.append(each)

                break
            elif "前缀" in item:
                listPre.append(each)
                break

    resultPre = []
    resultSux = []
    for item in listPre:
        tmp = ""
        for each in item:
            each = each.replace("<h3 class=\"pron\">", "")
            each = each.replace("</h3>", "")
            each = each.replace("\n", "")
            each = each.replace('\n', '').replace('\r', '')
            each = each.replace(" ", "")
            each = each.replace("<h3>", "")
            if each != "":
                tmp += each.strip() + ' '

        resultPre.append(tmp)

    for item in listSux:
        tmp = ""
        for each in item:
            each = each.replace("<h3 class=\"pron\">", "")
            each = each.replace("</h3>", "")
            each = each.replace("\n", "")
            each = each.replace('\n', '').replace('\r', '')
            each = each.replace(" ", "")
            each = each.replace("<h3>", "")
            if each != "":
                tmp += each.strip() + ' '

        resultSux.append(tmp)

    return resultPre, resultSux



if __name__ == '__main__':
    getPreOrSuf("contemporary")