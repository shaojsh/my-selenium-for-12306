# 导入seleium包
from time import sleep

from selenium import webdriver
# 实例化浏览器
driver = webdriver.Firefox()
# 打开项目-url(python中的\是转义字符)
driver.get("https://mail.qq.com/cgi-bin/loginpage")
driver.switch_to.frame('login_frame')
# partial link test 传入的值需要唯一性 模糊查询
element = driver.find_element_by_partial_link_text("忘了密").click()

# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()
