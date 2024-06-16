import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")

driver.find_element(By.LINK_TEXT, "compendiumdev").click()


