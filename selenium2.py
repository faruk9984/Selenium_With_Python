
# Selenium with Python Tutorial 3-WebDriver Commands

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")


print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)

# driver.close() # currently focused browser
driver.quit() # close all the open browsers
