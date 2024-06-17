import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")

time.sleep(2)

tf = driver.find_element(By.ID, "textbox1")

tf.clear()
time.sleep(2)

tf.send_keys("Dev dutta")
time.sleep(2)
tf.clear()
time.sleep(2)

tf.send_keys("selenium python")
time.sleep(2)
tf.clear()
time.sleep(2)

