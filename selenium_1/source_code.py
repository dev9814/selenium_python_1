import time

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://testpages.herokuapp.com/basic_web_page.html")
time.sleep(3)

html_source_code = driver.page_source

print(html_source_code)