# coding=utf-8
import csv
import re
import numpy as np
import pygal
from cleanData import cyqCleanData

def HJPDATA2():
    a = b = c = d = e = 0
    with open("cleanData.csv", "r", encoding="GBK") as file:
        dataList = cyqCleanData()
        # print(dataList)
        for i in dataList:
            sal = float(i[3])
            if sal <5000:
                a+=1
            elif sal >=5000 and sal <= 7000:
                b+=1
            elif sal >=7000 and sal <= 9000:
                c+=1
            elif sal >=9000 and sal <=11000:
                d+=1
            else:
                e+=1
            print(a,b,c,d,e)
            line = pygal.Pie()
            line.y_labels = (20,40,60,80,100)
            line.add("0-5000",a)
            line.add("5000-7000",b)
            line.add("7000-9000",c)
            line.add("9000-11000",d)
            line.add("11000+",e)
            line.render_to_file("饼状图.svg")
    print("饼状图绘制完成")