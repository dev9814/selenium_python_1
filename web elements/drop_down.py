import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")

time.sleep(3)

driver.find_element(By.ID, "drop1").click()

time.sleep(5)

driver.quit()