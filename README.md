# # tieba_spider

百度贴吧爬虫——获取页面信息
A way to get specific module of Baidu Tieba.

## Getting Started

该爬虫流程分为获取数据、数据整理、词云绘制三个文件中，数据的获取参见(spider_tieba_gener.py)，我使用面向对象的方法封装了一个爬虫类；数据整理见(spider_tieba_gener.py)；词云绘制见(wordclouddraw.py)。

由于数据文件过于庞大（原数据集1.2GB），我使用较小范围的帖子进行测试（20页帖子），读者可以修改spider_tieba_gener.py下的贴吧页数（Line 126)；用户也可以修改spider_tieba_gener.py下的贴吧名称（Line 123）。

爬取的数据保存在[name]/[name].csv中（name为贴吧名称，Line 123设置的，见上段），例：刀剑神域\刀剑神域.csv；内容汇总和分词绘图都保存在res中。

## Prerequisites

Python 3.X

| Python 模块 |        |
| --------- | ------ |
| jieba     | bs4    |
| wordcloud | pandas |

## What's New

* 本版本较上版本去除了openpyxl模块的依赖，选择使用Python自带模块csv；并将保存格式改为.csv文件，因此无xls或xlsx的最大行数限制

## Additional Documentation and Acknowledgments
1. [中文停用词表](https://github.com/goto456/stopwords)
2. [字体](https://www.100font.com/thread-562.htm)
