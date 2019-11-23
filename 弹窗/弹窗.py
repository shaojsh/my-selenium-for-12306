from selenium import webdriver

driver = webdriver.Chrome()

# 跳转网页
driver.get('https://.....')

# alert 弹窗常用方法  accept  dismiss 需要先切换窗口switch_to_alert
alEle = driver.switch_to.alert
alEle.dismiss()
alEle.accept()

# confirm 窗口




