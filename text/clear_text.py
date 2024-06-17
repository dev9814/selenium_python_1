import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")
time.sleep(2)

driver.find_element(By.ID, "textbox1").clear()
time.sleep(2)

driver.find_element(By.XPATH , "//h2[text()='Text Area Field Two']/following::textarea").clear()

# //*[@id="HTML11"]/div[1]/textarea