# coding=utf-8
import csv
import re
import numpy as np


def cyqCleanData():
    with open("Boss.csv", "r", encoding="utf-8") as file:
        dataList = []
        j = 0
        # 读取数据
        data = csv.reader(file)
        for row in data:  # each row is a list
            dataList.append(row)

        # print(dataList)
        for i in dataList:
            # 取第0列数据工资
            salary = i[0]
            # print(salary)
            if "K" in salary:
                # 正则表达式筛选出数字范围如：5-6K
                salary = re.findall(r"\d+-?\d", salary)
                # print(salary)
                # 取出第一列的数据，洗去K后面13薪
                salary = salary[0]
                # 提取左右数据，把“-”洗去
                salary = re.findall(r"\d+", salary)
                # 计算平均工资
                salary = (float(salary[0]) + float(salary[1])) / 2
                # 归一格式
                salary = salary * 1000
                # print(salary)

            elif "天" in salary:
                salary = re.findall(r"\d+-?\d+", salary)
                # print(salary)
                salary = salary[0]
                salary = re.findall(r"\d+", salary)
                salary = ((float(salary[0]) + float(salary[1])) / 2) * 26
                # print(salary)

            dataList[j].append(salary * 0.7)
            j += 1
        print(dataList)
    # dataList.to_csv("cleanData.csv")
    np.savetxt("cleanData.csv", dataList, delimiter=',', fmt='%s')
    return dataList

# cyqCleanData()
# cleanData()
