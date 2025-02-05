# tieba_spider

百度贴吧爬虫——获取页面信息<br>
![Display Picture](./res/tieba-wordcloud.png)<br>

## Getting Started

1. Run `spider_tieba_gener.py` to fetch web data. The file needs to be modified; details can be found in the comments.<br>
    > Modify `kw.json` to update `name` (Tieba name) and `page` (number of pages to crawl).
2. Save all comment information to a text file and run `wordcut.py`.<br>
3. For word cloud generation, run `wordclouddraw.py`.<br>
    > Remember to modify `userdict.txt` for word segmentation. If no custom dictionary is specified, you can clear the file and comment out the line `' # 导入自定义字典 '`.

## Prerequisites

Python 3.X

> [jieba](https://pypi.org/project/jieba/) Chinese word segmentation library<br>
> [bs4](https://beautiful-soup-4.readthedocs.io/en/latest/)<br>
> [wordcloud](https://pypi.org/project/wordcloud/) word cloud generation<br>
> [pandas](https://pandas.pydata.org/) Require openpyxl to read or write xls(x)<br>
> [openpyxl](https://openpyxl.readthedocs.io/en/stable/)


## Additional Documentation and Acknowledgments
1. [Chinese Stop Words](https://github.com/goto456/stopwords)<br>
2. [Font](https://www.100font.com/thread-562.htm)<br>
