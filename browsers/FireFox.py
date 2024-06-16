import time

from selenium import webdriver

driver = webdriver.Firefox()

driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/")

time.sleep(3)

driver.minimize_window()

driver.quit()



