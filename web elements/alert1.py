import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")

driver.find_element(By.ID, "alert1").click()

time.sleep(10)

driver.quit()