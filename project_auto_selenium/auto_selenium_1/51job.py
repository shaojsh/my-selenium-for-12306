from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
# 设置等待时间
driver.implicitly_wait(10)
driver.get("https://www.51job.com")
driver.find_element_by_id('kwdselectid').send_keys('python')
driver.find_element_by_id('work_position_click').click()
cities = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em[class = on]')
for one in cities:
    one.click()
sleep(3)
driver.find_element_by_id('work_position_click_center_right_list_category_000000_020000').click()
driver.find_element_by_id('work_position_click_bottom_save').click()
driver.find_element_by_css_selector("""button[onclick^="kwdGoSearch($('#kwdselectid').val());"]""").click()
jobs = driver.find_elements_by_css_selector('#resultList div[class = el]')
for job in jobs:
    print(job.text)
