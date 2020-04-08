import csv
import os

import pymysql


def downloadFromDB(bookname):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='remv_user', passwd="iloveRemV", db='remv')
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM %s_remv" % bookname)
    data = cur.fetchone()
    rowNUm = data[0]
    list_ = []
    for i in range(1, rowNUm + 1):
        cur.execute("SELECT word FROM %s_remv where id like %d" % (bookname, i))
        data = cur.fetchone()
        list_.append(data[0])

    conn.commit()
    conn.close()

    writeCSV(bookname, list_)


def writeCSV(bookname, list_):
    """
    [word,pos,translation,phonetic,collins,tag,definition,exchange]
    :param bookname: the csv going to be written
    :param list: contains a list of vocabularies
    :return: None
    """

    f = open("lib/res/word_Repository/csv/%s_remv.csv" % bookname, "w", encoding='utf-8', newline="")
    writer_ = csv.writer(f)

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='remv_user', passwd="iloveRemV", db='remv')
    cur = conn.cursor()

    for each in list_:
        word = each
        pos = ""
        translation = ""
        phonetic = ""
        collins = ""
        tag = ""
        definition = ""
        exchange = ""

        cur.execute("SELECT pos FROM stardict where word like '%s'" % each)
        data = cur.fetchone()
        if data is None:
            pos = ""
        elif data is not None:
            pos = data[0]

        cur.execute("SELECT translation FROM stardict where word like '%s'" % each)
        data = cur.fetchone()
        if data is None:
            translation = ""
        elif data is not None:
            translation = data[0]

        cur.execute("SELECT phonetic FROM stardict where word like '%s'" % each)
        data = cur.fetchone()
        if data is None:
            phonetic = ""
        elif data is not None:
            phonetic = data[0]

        cur.execute("SELECT collins FROM stardict where word like '%s'" % each)
        data = cur.fetchone()
        if data is None:
            collins = ""
        elif data is not None:
            collins = data[0]

        cur.execute("SELECT tag FROM stardict where word like '%s'" % each)
        data = cur.fetchone()
        if data is None:
            tag = ""
        elif data is not None:
            tag = data[0]

        cur.execute("SELECT definition FROM stardict where word like '%s'" % each)
        data = cur.fetchone()
        if data is None:
            definition = ""
        elif data is not None:
            definition = data[0]

        cur.execute("SELECT exchange FROM stardict where word like '%s'" % each)
        data = cur.fetchone()
        if data is None:
            exchange = ""
        elif data is not None:
            exchange = data[0]

        writer_.writerow([word, pos, translation, phonetic, collins, tag, definition, exchange])

    conn.commit()
    conn.close()
    f.close()

    print("下载离线库完成")