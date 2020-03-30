import openpyxl

import getTranslationFromYouDao
import time

wb = openpyxl.load_workbook("./初中/北师大初二下.xlsx")
ws = wb.active
count = 0

with open(r"./初中/北师大初二下.txt", "r") as f:
    line = f.readline()
    while line:
        str_ = ""
        strList = line.strip().split(" ")
        for i in range(len(strList)):
            if strList[i].strip().encode("utf-8").isalpha() \
                    and strList[i].strip() != "Lesson"\
                    and strList[i].strip() != "Unit":
                str_ += strList[i].strip() + " "
        if str_.strip():
            data = [str_.strip(), None]
            try:
                _, mean = getTranslationFromYouDao.translate(str_.strip())

                # deBug cell type error: a cell cannot take a two dimension array
                if mean:
                    data.append(mean[0])
                    print(mean[0])
                else:
                    data.append("NO MEANING FOUND")
            except:
                pass
            ws.append(data)

        line = f.readline()
        time.sleep(0.2)

wb.save("./初中/北师大初二下.xlsx")
