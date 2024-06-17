import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")
time.sleep(3)

text_of_element = driver.find_element(By.ID, "pah").text
print(text_of_element)


