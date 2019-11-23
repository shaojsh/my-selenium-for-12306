from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://baidu.com")

# 参数数字设置像素点
print("设置浏览器 480 800 显示")
sleep(3)
driver.set_window_size(480, 800)
sleep(3)
# 浏览器刷新
print("浏览器刷新")
driver.refresh()
sleep(3)
driver.quit()