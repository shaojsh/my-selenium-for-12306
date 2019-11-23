from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

# 获得cookie信息
cookie = driver.get_cookies()
# 将获得cookies打印
print(cookie)
driver.quit()