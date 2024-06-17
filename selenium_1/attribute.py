import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")
time.sleep(3)

attribute = driver.find_element(By.ID, "ta1").get_attribute("cols")
print(attribute)
time.sleep(3)

search = driver.find_element(By.XPATH, "//input[@name='q']").get_attribute("type")
print(search)
time.sleep(3)

driver.quit()
