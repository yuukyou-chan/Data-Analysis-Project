from selenium import webdriver
import csv
# 时间库，控制延迟时间
import time

def Spyder():
    url = "https://www.zhipin.com/"
    browser = webdriver.Chrome()
    browser.get(url)
    browser.find_element_by_css_selector(".ipt-search").send_keys("实习")
    browser.find_element_by_css_selector("#wrap > div.column-search-panel > div > div > div.search-form > form > button").click()
    browser.find_element_by_css_selector("#filter-box > div > div.condition-box > "
                                         "dl.condition-city.show-condition-district > dd > a:nth-child(6)").click()

    # 查看网页源码
    # print(browser.page_source)
    # 控制页数
    x = 1
    # 控制条数 1-30  31-60  61-90   91-120 ...
    j = 1
    # 循环翻页爬取数据
    # while结束条件是：是否到了最后一页
    # 判断是否到了最后一页标准：下一页按钮是否可用点击
    # 下一页不能点击：pn-next disabled
    # 下一页可点：pn-next
    # 当前源码中是否存在 “pn-next disabled”
    # 如果不存在，返回-1
    # 如果返回-1，说明不是最后一页
    while browser.page_source.find("next.disabled")==-1:
        liList = browser.find_elements_by_css_selector("#main > div > div.job-list > ul > li")
        # liList ----  [data,data,data,data,.....]
        # print(liList)
        for i in liList:
            # 获取薪酬标签
            work = i.find_element_by_css_selector("div > div.info-primary > div.primary-wrapper > div > "
                                                  "div.job-limit.clearfix > span").text
            # print(work)
            # # 获取职位名
            job = i.find_element_by_css_selector("div > div.info-primary > div.primary-wrapper").text
            # # 获取地区，学历标签
            area = i.find_element_by_css_selector("div.primary-wrapper > div > div.job-title > span.job-area-wrapper > span").text
            print(work,job,area)
            with open("Boss.csv", "a+", encoding="utf-8", newline="") as openFile:
                data = [work,job,area]
                csv.writer(openFile).writerow(data)
            # 数据条数+1
            j += 1
        print("第%s页数据下载完毕" % x)
        # # 点击下一页按钮
        browser.find_element_by_class_name("next").click()
        # # 页数+1
        x += 1
        # # 每次下载一页休息5秒钟（根据网速去估算）#J_bottomPage > span.p-num > a.pn-next
        time.sleep(5)