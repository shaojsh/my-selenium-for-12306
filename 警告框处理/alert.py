import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("https://www.baidu.com")

# 鼠标悬停至设置链接
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

# 打开搜素设置
driver.find_element_by_link_text("搜索设置").click()

# 保存设置
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(10)
# 接受警告框
driver.switch_to.alert.accept()

driver.quit()