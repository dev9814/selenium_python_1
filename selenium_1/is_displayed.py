import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://tutorialsninja.com/demo/")

driver.find_element(By.LINK_TEXT, "Register").send_keys(Keys.ENTER)

# //*[@id='top-links']/ul/li[2]/a/span[1]