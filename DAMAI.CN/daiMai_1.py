from mitmproxy import ctx, flow
from time import sleep

from selenium import webdriver

import inputdata
from modify_response import response


class daiMai_1:
    def buyDaiMaiTicket(self, num):
        # 反爬 设为开发者模式
        chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.add_argument('-headless')  # 设为无头模式
        chromeOptions.add_argument('disable-infobars')  # 去掉提示：Chrome正收到自动测试软件的控制
        chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以键值对的形式加入参数
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.driver.set_page_load_timeout(20)  # 设置模拟浏览器最长等待时间

        # 设置浏览器长宽
        self.driver.set_window_size(1200, 900)
        response(flow)
        # 告知数据源的路径
        path = "C://Users//86176//Desktop//inputData.xlsx"
        # 实例化对象
        inputData = inputdata.ReadExcel(path)
        self.dataList = inputData.dict_data()
        # 打开大麦网路径
        self.driver.get('https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F')
        response(flow)
        # 设置等待时间
        sleep(15)
        starTar = self.driver.find_element_by_xpath("//*[@class ='input-search']")
        starTar.clear()
        starTar.send_keys(self.dataList[num][1])

        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[1]').click()













