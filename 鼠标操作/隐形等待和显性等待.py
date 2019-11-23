from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# 拿到driver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# 跳转网页
driver.get('https://xdclass.net/#/index')
print(driver.title)

# 隐形等待，只需要设置一次就好，60秒之内还没加载好就会报错
# driver.implicitly_wait(60)

# 显性等待  (显性和隐形等待都设置时会选择时间比较长的 ：每隔0.5秒检查一次元素是否纯在 这个时间会持续5秒)
try:
    ele = WebDriverWait(driver, 5, 0.5).until(Ec.presence_of_all_elements_located(By.ID, "KW"))
except:
    print()
finally:
    print()


# 登录框
login_ele = driver.find_element_by_css_selector()