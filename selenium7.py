"""
#######################################################################################
# Selenium with Python Tutorial 11-Working with Links | Operations on Web Links | Handling Links

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="chromedriver.exe")

# driver.get("http://ww7.demoaut.com/")
driver.get("https://www.npr.org/")

links=driver.find_elements(By.TAG_NAME,"a")
print("total link: ",len(links))

for link in links:
    print(link.text)

driver.find_element(By.LINK_TEXT,"News").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"New").click()
driver.find_element(By.LINK_TEXT,"Business").click()



#######################################################################################

# Selenium with Python Tutorial 12-How to handle Alerts/Popups || Switching to Alerts/Popups

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

drver=webdriver.Chrome(executable_path="chromedriver.exe")

drver.get("http://testautomationpractice.blogspot.com/")

drver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(3)

drver.switch_to.alert.accept() # ok button hisabe kaj kor
#drver.switch_to.alert.dismiss() # cancle button hisabe kaj kore


"""

#######################################################################################

# Selenium with Python Tutorial 13-How to handle Frames/iFrames | Switch between the frames

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html/body/header/nav/div[1]/div[1]/ul/li[6]").click()
time.sleep(3)



