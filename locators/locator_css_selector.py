
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")

driver.find_element(By.CSS_SELECTOR , "input[value='Login']").click()

# //*[@id='menu']/div[2]/ul/li[1]