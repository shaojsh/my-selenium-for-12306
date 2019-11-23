# 无法获得多窗口句柄？
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://wwww.baidu.com")

# 获得百度检索窗口句柄
searchWindows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
time.sleep(10)
# 获取当前所有打开窗口的句柄
all_handles = driver.window_handles
print(all_handles)
# 进入注册页面
for handle in all_handles:
    if handle != searchWindows:
        driver.switch_to.window(handle)
        print("now register window")
        driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
        driver.find_element_by_name("account").send_keys("sjs")
        driver.find_element_by_name("password").send_keys("pwd")
        time.sleep(2)

        driver.quit()
