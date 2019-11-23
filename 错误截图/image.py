from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# 拿到driver
driver = webdriver.Chrome()

# 跳转网页
driver.get('https://xdclass.net/#/index')
print(driver.title)

# 休眠3秒
sleep(3)

try:
    driver.find_elements_by_id("xdclass").click()
except:
    driver.get_screenshot_as_file('./error.png')