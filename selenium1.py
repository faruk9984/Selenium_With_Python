
# Selenium with Python Tutorial 2-How to Run Tests on Chrome, Firefox & IE Browsers

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="chromedriver.exe")
# driver=webdriver.Firefox(executable_path="geckodriver.exe")

# driver.get("http://newtours.demoaut.com/")
driver.get("https://www.w3schools.com/html/default.asp")

print(driver.title)# page er title show korbe
print(driver.current_url)# current page er url show korbe
print(driver.page_source)# page er sob code show korbe
driver.close()# close the browser



