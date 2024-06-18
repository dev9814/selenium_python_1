import time

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
time.sleep(3)


# driver.save_screenshot("login.png")

# driver.get_screenshot_as_file("C:\\Users\\hp\\PycharmProjects\\Python_Selenium_QAFox\\Screenshots\\shot1.png")


driver.get_full_page_screenshot_as_png()