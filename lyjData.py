# coding=utf-8

import pygal
from cleanData import cyqCleanData


def LYJDATA():
    a = b = c = d = e = 0
    j = 0
    with open("cleanData.csv", "r", encoding="GBK") as file1:
        dataList = cyqCleanData()
        # print(data)
        for k in dataList:
            edu = k[1]
            if "在校/应届学历不限" in edu:
                a += 1
            elif "在校/应届本科" in edu:
                b += 1
            elif "在校/应届硕士" in edu:
                c += 1
            elif "博士" in edu:
                d += 1
            else:
                e += 1
            print(a, b, c, d, e)
            line = pygal.Pie()
            # line.x_title = ("学历")
            # line.y_title = ("数量 ")
            # line.x_labels = ["在校/应届学历不限,在校/应届本科,在校/应届硕士,博士,其他"]
            line.y_labels = [0, 40, 80, 120, 160, 200]
            line.title = "学历要求分析图"
            line.add("在校/应届学历不限", a)
            line.add("在校/应届本科", b)
            line.add("在校/应届硕士", c)
            line.add("博士", d)
            line.add("其他", e)
            line.render_to_file("饼状图.svg")
    print("结束")
