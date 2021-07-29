# coding=utf-8
# 可视化窗口
from tkinter import *
from tkinter import messagebox

from average import cyqAverrage
from BossSpyder import Spyder
from ciYun import ciyun
from cleanData import cyqCleanData
from hjpData import HJPDATA
from hjpData2 import HJPDATA2
from lyjData import LYJDATA
from lyjData2 import LYJDATA2


def mainMenu():
    # 定义窗口
    root = Tk()
    # 窗口标题
    root.title("BOSS直聘网数据")
    # 窗口尺寸
    root.geometry("560x600")
    # 添加图片
    # photo = PhotoImage(file="mudan.png")
    # label6 = Label(root,image=photo)
    # label6.place(relx=0,rely=0,relwidth=0.01,relheight=0.01)
    # 添加文字组件

    label7 = Label(root, text="BOSS直聘数据爬取", font="100")
    label7.place(relx=0.17, rely=0.07)
    label8 = Label(root, text="数据清洗", font="100")
    label8.place(relx=0.3, rely=0.17)
    label1 = Label(root, text="学历要求分析", font="100")
    # 根据百分比计算位置
    label1.place(relx=0.25, rely=0.27)
    label2 = Label(root, text="岗位需求分析", font="100")
    label2.place(relx=0.25, rely=0.37)
    label3 = Label(root, text="各城市招聘数的数据分析", font="100")
    label3.place(relx=0.08, rely=0.47)
    label4 = Label(root, text="工资区间的数据分析", font="100")
    label4.place(relx=0.14, rely=0.57)
    label5 = Label(root, text="词云展示", font="100")
    label5.place(relx=0.37, rely=0.67)
    label6 = Label(root, text="平均工资", font="100")
    label6.place(relx=0.3, rely=0.77)
    #
    # 按钮组件   command=lambda: 点击按钮，调用对应函数
    btn7 = Button(root, text="运行爬虫", command=lambda: Spyder())
    btn7.place(relx=0.48, rely=0.06, relwidth=0.4, relheight=0.065)
    btn8 = Button(root, text="数据清洗", command=lambda: cyqCleanData())
    btn8.place(relx=0.48, rely=0.16, relwidth=0.4, relheight=0.065)
    btn1 = Button(root, text="生成饼状图", command=lambda: LYJDATA())
    btn1.place(relx=0.48, rely=0.26, relwidth=0.4, relheight=0.065)
    btn2 = Button(root, text="生成柱状图", command=lambda: LYJDATA2())
    btn2.place(relx=0.48, rely=0.36, relwidth=0.4, relheight=0.065)
    btn3 = Button(root, text="生成柱状图", command=lambda: HJPDATA())
    btn3.place(relx=0.48, rely=0.46, relwidth=0.4, relheight=0.065)
    btn4 = Button(root, text="生成饼状图", command=lambda: HJPDATA2())
    btn4.place(relx=0.48, rely=0.56, relwidth=0.4, relheight=0.065)
    btn5 = Button(root, text="生成词云", command=lambda: ciyun())
    btn5.place(relx=0.48, rely=0.66, relwidth=0.4, relheight=0.065)
    btn6 = Button(root, text="生成柱状图", command=lambda: cyqAverrage())
    btn6.place(relx=0.48, rely=0.76, relwidth=0.4, relheight=0.065)
    # messagebox.showinfo("提示", "BOSS直聘网数据生成成功")
    # 加载窗口
    root.mainloop()


mainMenu()
