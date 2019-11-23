from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://mail.qq.com/cgi-bin/loginpage")
driver.switch_to.frame("login_frame")

driver.find_element_by_name("u").send_keys("2319898127@qq.com")
driver.find_element_by_name("p").send_keys("1057241445")

sleep(3)
driver.quit()
