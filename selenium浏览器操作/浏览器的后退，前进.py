from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

# 访问百度首页
firstUrl = "http://baidu.com"
print("now access %s" % firstUrl)
driver.get(firstUrl)

# 访问新闻页面
secondUrl = "http://news.baidu.com"
print("now access %s" % secondUrl)
driver.get(secondUrl)

# 回退到百度首页
print("now access %s" % firstUrl)
driver.back()

# 前进到新闻业
print("now access %s" % secondUrl)
driver.forward()

sleep(3)
driver.quit()