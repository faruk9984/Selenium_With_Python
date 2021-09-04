"""
# Selenium with Python Tutorial 6-WebDriver Implicit wait
from selenium import webdriver

driver=webdriver.Chrome(executable_path='chromedriver.exe')

driver.get("http://newtours.demoaut.com/")
# driver.get("https://profile.w3schools.com/")
driver.implicitly_wait(10)

# assert "demoaut.com" in driver.title
assert "demoaut.com" in driver.title

driver.find_element_by_name("email").send_keys("mercury")
driver.find_element_by_name("current-password").send_keys("mercury")
driver.find_element_by_name("Login").click()

"""

# Selenium with Python Tutorial 7-WebDriver Explicit wait

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.expedia.com/")

# driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element(By.ID,"tab-flight-tab-hp").click()


driver.find_elements(By.ID,"flight-origin-hp-flight").send_keys("SFO")
time.sleep(2)
driver.find_element(By.ID,"flight-destination-hp-flight").send_keys('NYC')

driver.find_element(By.ID,"flight-departing-hp-flight").clear()
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys('10/10/2021')
driver.find_element(By.ID,"flight-returning-hp-flight").clear()
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys('15/10/2021')

driver.find_element(By.XPATH,"//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click()

# explicit wait
wait=WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='wizard-flight-pwa-1']")))
element.click()
time.sleep(3)

driver.quit()


