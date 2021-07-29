# coding=utf-8

import pygal
from cleanData import cyqCleanData

def HJPDATA():

    a = b = c = d = e = f = 0
    with open("cleanData.csv", "r", encoding="GBK") as file1:
        dataList = cyqCleanData()
        # print(data)
        for k in dataList:
            reigon = k[2]
            if "北京" in reigon:
                a += 1
            elif "苏州" in reigon:
                b += 1
            elif "杭州" in reigon:
                b += 1
            elif "深圳" in reigon:
                c += 1
            elif "上海" in reigon:
                d += 1
            elif "广州" in reigon:
                e += 1
            else:
                f += 1
            # print(a, b, c, d, e, f)
            line = pygal.Bar()
            line.x_title = ("城市")
            line.y_title = ("岗位数")
            # line.x_labels = ("北京","苏州，杭州","深圳","上海","广州","其他")
            line.y_labels = [0, 20, 40, 60, 80, 100]
            line.title = "不同城市岗位数分析图"
            line.add("北京", a)
            line.add("苏州，杭州", b)
            line.add("深圳", c)
            line.add("上海", d)
            line.add("广州", e)
            line.add("其他", f)
            line.render_to_file("城市岗位数量需求柱状图.svg")
    print("图片成功生成！")
# HJPDATA()