import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")
time.sleep(2)

current_url1 = driver.current_url
print(current_url1)

time.sleep(3)

driver.find_element(By.LINK_TEXT, "jqueryui").send_keys(Keys.ENTER)
# driver.find_element(By.XPATH , "//*[@id='LinkList1']/div/ul/li[1]/a").send_keys(Keys.ENTER)
time.sleep(3)

current_url2 = driver.current_url
print(current_url2)

