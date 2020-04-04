import re
from urllib import request

res = request.urlopen(
    r"https://github.com/ArmandXiao/RemV/blob/master/PyQt5_GUI/RemV_Package/lib/version.txt",
    timeout=3)
html = res.read().decode("utf-8")

findVersion = re.compile(
    "(<td id=\"LC1\" class=\"blob-code blob-code-inner js-file-line\">)(.*?)(</td>)")
newVersion = findVersion.findall(html)[0][1]
print(newVersion)