import pandas
import os

# 自己数据文件所在吧名
directory = "汽车吧"
# 保存内容至文本文件
f = open('words.txt',mode='a+',encoding='UTF-8')

for file in os.listdir(directory):
    data = pandas.read_excel(directory+"/"+file,sheet_name="汽车")
    data.dropna(subset=['大致内容'], inplace=True)
    # print(data)

    for item in data['大致内容']:
        f.write(str(item))

f.close()