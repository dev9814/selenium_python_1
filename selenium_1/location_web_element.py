import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://tutorialsninja.com/demo/")
time.sleep(3)

element_location = driver.find_element(By.NAME , "search").location

print(element_location)
print('--------')
print('x: ', element_location.get('x'))
print('y: ', element_location.get('y'))

element_location_x = driver.find_element(By.NAME , "search").rect
time.sleep(3)

print(element_location_x)

