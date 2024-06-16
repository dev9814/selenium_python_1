import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")

driver.find_element(By.NAME , "q").send_keys("google.com")

time.sleep(5)

driver.quit()