
# Selenium with Python Tutorial 4-WebDriver Navigational Commands

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
print(driver.title) # FR title

driver.get("http://pavantestingtools.blogspot.in/")
time.sleep(5)
print(driver.title) # tt ->testing tools title

driver.back()
time.sleep(5)
print(driver.title) # FR title

driver.forward()
time.sleep(5)
print(driver.title) # tt ->testing tools title
driver.close()