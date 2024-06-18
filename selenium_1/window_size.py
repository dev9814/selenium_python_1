import time

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")
time.sleep(3)

driver.set_window_size(300, 600)


