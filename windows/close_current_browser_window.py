import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")
time.sleep(3)

driver.find_element(By.LINK_TEXT, "Open a popup window").send_keys(Keys.ENTER)
time.sleep(3)

driver.current_window_handle



driver.close()
