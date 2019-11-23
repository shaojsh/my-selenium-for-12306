from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://wwww.baidu.com")

# 清除文本 clear()
driver.find_element_by_id("kw").clear()

# 模拟键盘输入 send_keys()
driver.find_element_by_id("kw").send_keys("hello world")
sleep(3)

# 单击元素 click()
driver.find_element_by_id("su").click()
sleep(3)

driver.quit()

# 其他常用方法： size:返回元素尺寸
# text 获取元素文本
# get_attribute(name):获取属性值
# is_displayed():设置元素是否用户可见
