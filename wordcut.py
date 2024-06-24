import numpy
import pandas
import json

# 自己数据文件所在目录
jsn = json.load(open('kw.json', 'r', encoding="UTF-8"))
# 保存内容至文本文件
fp = open(f'res/{jsn['name']}.txt', mode='w', encoding='UTF-8')

data = pandas.read_excel('res' + f"/{jsn['name']}吧.xlsx")

for row in data.values:
    if row[4] is not numpy.nan:
        fp.write(str(row[4]))
        fp.write('\n')

fp.close()