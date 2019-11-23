from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(By.ID))
element.send_Keys("selenium")
driver.quit()