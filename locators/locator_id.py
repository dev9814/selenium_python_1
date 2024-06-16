import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# driver.maximize_window()

driver.get("https://omayo.blogspot.com/")

driver.find_element(By.ID, "ta1").send_keys("this is a text field area")

time.sleep(5)

driver.quit()