
from selenium.webdriver import ActionChains
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("https://www.baidu.com")

# 鼠标悬停至设置链接
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()
