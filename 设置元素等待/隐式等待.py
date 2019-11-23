from time import ctime
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

driver = webdriver.Firefox()

# 设置隐式等待
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys('selenium')
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()
