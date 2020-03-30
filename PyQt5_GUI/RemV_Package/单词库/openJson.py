import json
import openpyxl

wb = openpyxl.load_workbook("高中词汇.xlsx")
ws = wb.active


# 由于文件中有多行，直接读取会出现错误，因此一行一行读取
file = open("BEC_2.json", 'r', encoding='utf-8')
papers = []
tranNum = 0
posNum = 0
engTran = 0
for line in file.readlines():

    dic = json.loads(line)

    mean = dic["content"]["word"]["content"]["trans"][0]["tranCn"]
    try:
        pos = dic["content"]["word"]["content"]["trans"][0]["pos"]
    except:
        pos = " "
    word = dic["content"]["word"]["wordHead"]

    try:
        if dic["content"]["word"]["content"]["trans"][0]["tranOther"]:
            mean += "\n" + dic["content"]["word"]["content"]["trans"][0]["tranOther"]
    except:
        pass
    data = [word, pos, mean]
    ws.append(data)

    papers.append(dic)

wb.save("高中词汇.xlsx")
