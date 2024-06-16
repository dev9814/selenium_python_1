import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")

driver.find_element(By.CLASS_NAME, "dropbtn").click()

time.sleep(5)

driver.quit()