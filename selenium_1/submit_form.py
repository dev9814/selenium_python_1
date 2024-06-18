import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
time.sleep(3)

driver.find_element(By.ID , "input-email").send_keys("ddd")
time.sleep(2)

driver.find_element(By.ID, "input-password").send_keys("123")
time.sleep(2)


