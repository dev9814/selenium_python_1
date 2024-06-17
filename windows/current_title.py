import time

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")
time.sleep(2)

web_page_title = driver.title
print(web_page_title)
