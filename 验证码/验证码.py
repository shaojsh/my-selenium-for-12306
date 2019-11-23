# 1. ocr识别      tesseract-orc 谷歌开源
# 2. ai人工智能   tensorFlow 谷歌开源
# 3. 绕过（主流）   一： 万能验证码  二： 开发人员关闭 三：操作cookie(主流)
from time import sleep

from selenium import webdriver
driver = webdriver.Chrome()

# 跳转网页
driver.get('https://xdclass.net/#/index')
print(driver.title)

driver.add_cookie({"name": "name", "value": "yangyangyang"})
driver.add_cookie({"name": "token", "value": "xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvMTcuanBlZyIsImlkIjoxNTA5NiwibmFtZSI6InNodWFpMjAxOSIsImlhdCI6MTU3NDUwMzQxOSwiZXhwIjoxNTc1MTA4MjE5fQ.M5l8T1-eIK8GnzjbEeU-b292Dz5UYtwwqZY8LCcjAsE"})
driver.refresh()
sleep(3)