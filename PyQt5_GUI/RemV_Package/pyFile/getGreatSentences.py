import linecache
import random


def getSentences():
    """
    Get random great sentences from repository.
    :return: a str that contains English version, a str that contains Chinese version of great sentence.
    """
    path_ = r"lib/res/great_sentences.txt"
    list_ = linecache.getlines(path_)
    rand = random.randint(0, len(list_) - 2)

    while (list_[rand].strip() == "") or (list_[rand + 1].strip() == ""):
        rand = random.randint(0, len(list_) - 2)
    engStr = list_[rand].strip()
    chiStr = list_[rand + 1].strip()

    for i in engStr:
        if not (ord("A") <= ord(i) <= ord("z")) and i != " ":
            engStr = engStr.replace(i, "")

    return engStr.strip() + ".", chiStr

