# coding=utf-8
import csv
# jieba分词器，将一句话的词云分出来
import jieba
# 算法运算库
import numpy
# 图像库   pillow
from PIL import Image
# 词云库  wordcloud
from wordcloud import WordCloud
from cleanData import cyqCleanData


def ciyun():
    # with open("jd.csv","r",encoding="utf-8") as file:
    data = cyqCleanData()
    # print(data)
    # 定义字符串，装所有的简介
    comments = ""
    # 数据结果  [价格，店铺名，简介]
    for i in data:
        # print(i)
        comments += i[2]
    # print(comments)
    # 通过jieba分词器把词语分离出来，用空格连结
    cutWord = "  ".join(jieba.cut(comments))
    # print(cutWord)
    # 读取图片模型
    bgImg = numpy.array(Image.open("l.png"))
    cloud = WordCloud(
        # 字体类型，本地系统文件的文字类型
        font_path="‪‪C:\Windows\Fonts\STKAITI.TTF",
        # 生成词云时背景颜色
        background_color="beige",
        # 参考图片
        mask=bgImg,
    ).generate(cutWord)
    # 生成词云图片
    cloud.to_file("ll.png")
    print("词云生成完毕")

# ciyun()