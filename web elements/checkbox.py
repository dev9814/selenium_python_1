import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")

time.sleep(3)

driver.find_element(By.ID, "checkbox1").click()

time.sleep(3)

driver.find_element(By.ID, "checkbox2").click()

time.sleep(5)

driver.quit()