from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.implicitly_wait(8)
driver.get("https://www.baidu.com")

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)

# 截取当前窗口
driver.get_screenshot_as_file("D:\\2000.jpg")

driver.quit()