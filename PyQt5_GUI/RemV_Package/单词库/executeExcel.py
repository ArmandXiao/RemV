import openpyxl

wb = openpyxl.load_workbook(r"C:\Users\Armand\PycharmProjects\RemV\PyQt5_GUI\RemV_Package\单词库\新GRE官方词汇表格完整版.xlsx")
ws = wb.active
try:  # ws may be a blank page
    for eachRow in ws:
        str_ = str(eachRow[4].value) + ", " + str(eachRow[3].value)
        eachRow[4].value = str_
except:
    pass

wb.save(r"C:\Users\Armand\PycharmProjects\RemV\PyQt5_GUI\RemV_Package\单词库\新GRE官方词汇.xlsx")