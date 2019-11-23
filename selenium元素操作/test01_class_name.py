from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://mail.qq.com/cgi-bin/loginpage")

driver.switch_to.frame("login_frame")
driver.find_element_by_class_name("inputOuter").send_keys("hello world")

sleep(3)
driver.quit()
