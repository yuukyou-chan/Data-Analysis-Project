# coding=utf-8

import pygal
from cleanData import cyqCleanData


def LYJDATA2():
    a = b = c = d = e = 0
    with open("cleanData.csv", "r", encoding="GBK") as file1:
        dataList = cyqCleanData()
        # print(data)
        for k in dataList:
            edu = k[1]
            if "工程师" in edu:
                a += 1
            elif "分析师" in edu:
                b += 1
            elif "研究员" in edu:
                c += 1
            elif "运营" in edu:
                d += 1
            else:
                e += 1
            print(a, b, c, d, e)
            line = pygal.Bar()
            # line.x_title = ("学历")
            # line.y_title = ("数量 ")
            # line.x_labels = ["在校/应届学历不限,在校/应届本科,在校/应届硕士,博士,其他"]
            line.y_labels = [0,40,80,120,160,200]
            line.title = "岗位需求分析图"
            line.add("工程师", a)
            line.add("分析师", b)
            line.add("研究员", c)
            line.add("运营", d)
            line.add("其他", e)
            line.render_to_file("柱状图.svg")
    print("结束")