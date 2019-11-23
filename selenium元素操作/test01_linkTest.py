# 导入seleium包
from time import sleep

from selenium import webdriver
# 实例化浏览器
driver = webdriver.Firefox()
# 打开项目-url(python中的\是转义字符)
driver.get("https://mail.qq.com/cgi-bin/loginpage")
# driver.switch_to.frame('login_frame')
# 找到用户名文本框
element = driver.find_element_by_link_text("关于腾讯").click()
# 给文本框传值
element.send_keys("2319898127@qq.com")

pwd = driver.find_element_by_id("p")
pwd.send_keys("1057241445")
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()
