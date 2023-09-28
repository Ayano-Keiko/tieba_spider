import csv

# 自己数据文件所在目录
directory = "刀剑神域"
# 保存内容至文本文件
fp = open('res/words(less).txt',mode='w',encoding='GB18030')

reader = csv.reader(open("刀剑神域\刀剑神域(less).csv", "r", encoding="GB18030", newline=""))
index = 1

for row in reader:
    if index > 1:
        fp.write(row[3])
        fp.write('\n')

    index += 1

fp.close()
