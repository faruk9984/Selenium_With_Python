
# Selenium with Python Tutorial 5-WebDriver Conditional Commands

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="chromedriver.exe")

# driver.get("http://ww12.demoaut.com/")
driver.get("https://profile.w3schools.com/")

user_ele=driver.find_element_by_name("email")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

pass_ele=driver.find_element_by_name("current-password")
print(pass_ele.is_displayed())
print(pass_ele.is_enabled())

user_ele.send_keys("faruk")
pass_ele.send_keys("faruk")
driver.find_element_by_name("login").click()

roundtip_radio=driver.find_element_by_css_selector("input[value=roundtrip]")
print(roundtip_radio.is_selected())

onetip_radio=driver.find_element_by_css_selector("input[value=oneway]")
print(onetip_radio.is_selected())
