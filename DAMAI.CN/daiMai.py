from time import sleep
import daiMai
from selenium import webdriver


class daiMai1:
    def buyDaiMaiTicket(self):
        # 反爬 设为开发者模式
        chromeOptions = webdriver.ChromeOptions()
        # # chromeOptions.add_argument('-headless')  # 设为无头模式

        chromeOptions.add_argument('disable-infobars')  # 去掉提示：Chrome正收到自动测试软件的控制
        chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以键值对的形式加入参数
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.driver.set_page_load_timeout(30)  # 设置模拟浏览器最长等待时间
        self.driver.get('https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F%3Futm_source%3Dsearch%26utm_medium%3Dbaidupc%26utm_content%3Dpmarket_yhcpyyb%26utm_campaign%3Dalink_bdsem_xg_shouye_4203')
        sleep(30)
        self.driver.find_element_by_css_selector('.input-search').send_keys('周杰伦')


if __name__ == '__main__':
    daiMai1 = daiMai1()
    daiMai1.buyDaiMaiTicket()
