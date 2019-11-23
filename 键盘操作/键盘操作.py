from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# 输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")

# 删除按钮 KeyS.BACK_SPACE
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
sleep(3)

# 空格 Keys.SPACE
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")

# Ctrl+a
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "A")
sleep(3)
# Ctrl + x
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "x")
sleep(3)
# ctrl + v
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "V")
sleep(3)
# 回车键
driver.find_element_by_id("kw").send_keys(Keys.ENTER)
sleep(3)

driver.quit()