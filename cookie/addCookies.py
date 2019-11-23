from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.youdao.com")

# 向cookie name value添加会话信息
driver.add_cookie({'name': 'key_aaaaaa', 'value': 'value-bbb'})

for cookie in driver.get_cookies():
    print('%s -> %s' % (cookie['name'], cookie['value']))

driver.quit()