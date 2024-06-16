import time

from selenium import webdriver

driver = webdriver.Firefox()

time.sleep(5000)

driver.maximize_window()

time.sleep(5000)

driver.quit()

