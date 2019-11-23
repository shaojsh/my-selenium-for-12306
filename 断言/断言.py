from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

print('BEFORE SEARCH======================')

# 打印页面ttle
title = driver.title
print(title)

# 打印当前页面的URL
now_url = driver.current_url
print(now_url)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(1)

print("AFTER SEARCH======================")
# 打印页面ttle
title = driver.title
print(title)

# 打印当前页面的URL
now_url = driver.current_url
print(now_url)
# 获取结果数目
user = driver.find_element_by_class_name('nums').text
print(user)

driver.quit()

