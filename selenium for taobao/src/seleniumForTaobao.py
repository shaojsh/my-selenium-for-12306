from selenium import webdriver
class taobao:
    def shopping(self,num):
        # 反爬 设为开发者模式
        chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.add_argument('-headless')  # 设为无头模式
        chromeOptions.add_argument('disable-infobars')  # 去掉提示：Chrome正收到自动测试软件的控制
        chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以键值对的形式加入参数
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)

        self.driver.get()

