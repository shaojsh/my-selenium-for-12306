from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.implicitly_wait(8)
driver.get("https://www.baidu.com")

# 鼠标悬停
driver.find_element_by_link_text('设置').click()
sleep(1)
# 打开检索设置
driver.find_element_by_link_text("搜索设置").click()
sleep(2)
sel = driver.find_element_by_xpath("//select[@id='nr']")
Select(sel).select_by_value('50')
sleep(2)
driver.quit()