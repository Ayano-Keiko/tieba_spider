'''
绘制词云图
'''

import jieba
import wordcloud
import pandas

def cut_word(path):
    file = open(path, "r", encoding='UTF-8')
    txt = file.read()

    # 导入自定义字典
    #jieba.load_userdict("userdict.txt")

    txt_cut = jieba.lcut(txt)

    return txt_cut

def fix_data(wordcut):
    data = pandas.read_csv("stopwords-master/cn_stopwords.txt", header=None, names=['words'])
    excludes = list(data['words'].values)
    counts = {}

    for item in wordcut:
        if len(item) == 1:
            continue
        else:
            counts[item] = counts.get(item, 0) + 1

    for exclude in excludes:
        try:
            del counts[exclude]
        except KeyError:
            continue

    return counts

def to_list(items):
    items = list(items.items())

    items.sort(key=lambda x: x[1],reverse=True)

    # for i in range(20):
    #     print("{}-->{}".format(items[i][0],items[i][1]))
    return items

def save_wordFreq(items):
    data = pandas.DataFrame(data=items,columns=["name","val"])

    data.to_csv("freq.csv",encoding="GBK")

    return data

def draw_pic(item):
    w = wordcloud.WordCloud(width=1960, height=1080, font_path="XingCao.ttf",
                            background_color="#FFFFFF")
    w.generate_from_frequencies(item)
    w.to_file("tieba-wordcloud.png")

def main():
    file = "words1.txt"

    # 进行分词处理
    txt_cut = cut_word(file)

    # 分词后词语预处理，包括统计词频和删除停用词
    items = fix_data(txt_cut)

    # 将字典格式的词频转换为列表格式，并排序
    list_items = to_list(items)
    save_wordFreq(list_items)

    # 绘制词云图
    draw_pic(items)

if __name__ == "__main__":
    main()