# coding=gbk
import pygal

from cleanData import cyqCleanData
import matplotlib.pyplot as plt
from pyecharts.charts import Bar
from pyecharts import options as opts


def cyqAverrage():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    a = b = c = d = e = f = g = 0
    a1 = b1 = c1 = d1 = e1 = f1 = g1 = 0
    j = 0
    data = []
    data = cyqCleanData()
    print(cyqCleanData())
    for k in data:
        reigon = k[2]
        if "北京" in reigon:
            a = a + k[3]
            a1 += 1
        elif "苏州" in reigon:
            b = b + k[3]
            b1 += 1
        elif "杭州" in reigon:
            b = b + k[3]
            b1 += 1
        elif "深圳" in reigon:
            c = c + k[3]
            c1 += 1
        elif "上海" in reigon:
            d = d + k[3]
            d1 += 1
        elif "广州" in reigon:
            e = e + k[3]
            e1 += 1
        else:
            f = f + k[3]
            f1 += 1
        print(a, b, c, d, e, f)
        print(a1, b1, c1, d1, e1, f1)
        print(d)
    aver = [a / a1, b / b1, c / c1, d / d1, e / e1, f / f1]
    aver = list(map(int, aver))
    city = ["北京", "苏杭", "深圳", "上海", "广州", "其他"]
    # 画图
    bar = (
        Bar()
            .add_xaxis(xaxis_data=city)
            .add_yaxis("实习工资", aver)
            .reversal_axis()
            .set_global_opts(title_opts=opts.TitleOpts(title="各大城市实习工资"))
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    )
    bar.render("平均工资图.html")


# print("图片成功生成")

# cyqAverrage()
