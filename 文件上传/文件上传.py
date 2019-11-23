from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
url = "file:///C:/Users/86176/Desktop/1.html"
driver.get(url)

# 定位上传按钮添加本地文件
driver.find_element_by_name("file").send_keys("file:///C:/Users/86176/Desktop/1.html")
sleep(2)
driver.quit()