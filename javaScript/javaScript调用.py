from time import sleep

from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://wwww.baidu.com")

# 设置浏览器大小 set_window_size
driver.set_window_size(500, 500)

# 搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

# 通过javascript设置浏览器滚动条位置
js = "window.scrollTo(100,450)"
driver.execute_script(js)
sleep(3)
driver.quit()