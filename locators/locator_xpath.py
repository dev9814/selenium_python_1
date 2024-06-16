import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://demoqa.com/buttons")

driver.find_element(By.XPATH, "//button[@id='rightClickBtn']").click()
