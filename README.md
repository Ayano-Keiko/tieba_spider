# tieba_spider

百度贴吧爬虫——获取页面信息<br>
A way to get specific module of Baidu Tieba.<br>

## Getting Started

1. 运行spider_tieba_gener.py获取网页数据，需要修改文件，详情可查看注释<br>
    > 修改kw.json内name(贴吧名)和page(爬取页数)
2. 将所有评论信息保存至一个文本文件，运行wordcut.py<br>
3. 词云绘制，运行wordclouddraw.py<br>
    > 分词记得修改userdict.txt，如果没有指定自定义分词字典可全清空并注释' # 导入自定义字典 '这行

## Prerequisites

Python 3.X

> [jieba](https://pypi.org/project/jieba/)<br>
> [bs4](https://beautiful-soup-4.readthedocs.io/en/latest/)<br>
> [wordcloud](https://pypi.org/project/wordcloud/)<br>
> [pandas](https://pandas.pydata.org/) 需要openpyxl引擎<br>
> [opencv-python](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)<br>
> some build-in modules like time, csv, json<br>


## Additional Documentation and Acknowledgments
1. [中文停用词表](https://github.com/goto456/stopwords)<br>
2. [字体](https://www.100font.com/thread-562.htm)<br>
