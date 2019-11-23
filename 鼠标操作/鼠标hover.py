from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# 拿到driver
driver = webdriver.Chrome()

# 跳转网页
driver.get('https://xdclass.net/#/index')
print(driver.title)

# 休眠3秒
sleep(3)

menu_ele = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/ul/li[1]')
ActionChains(driver).move_to_element(menu_ele).perform()

# 选中子菜单
sub_menu = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/a[1]')
sleep(2)
sub_menu.click()