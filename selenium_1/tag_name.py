import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")
time.sleep(3)

element_tag = driver.find_element(By.ID, "pah").tag_name

print(element_tag)