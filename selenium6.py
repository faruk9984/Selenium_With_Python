
# Selenium with Python Tutorial 8-Working with Input box/Test Box
# Selenium with Python Tutorial 10-Working with Drop-down list


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="chromedriver.exe")


driver.get("http://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

inputboxs=driver.find_elements(By.CLASS_NAME,"text_field")
print(len(inputboxs))

status=driver.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print(status)
status=driver.find_element(By.ID,'RESULT_TextField-1').is_enabled()
print(status)

driver.find_element(By.ID,'RESULT_TextField-1').send_keys("pavan")
driver.find_element(By.ID,'RESULT_TextField-2').send_keys("kumar")

driver.find_element_by_id("RESULT_TextField-3").send_keys('12345678')
driver.find_element_by_id("RESULT_TextField-4").send_keys('Bangladesh')
driver.find_element_by_id("RESULT_TextField-5").send_keys('Dhaka')
driver.find_element_by_id("RESULT_TextField-6").send_keys('faruk@gmail.com')


# status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
# print(status)
# driver.find_element_by_id("RESULT_RadioButton-7_0").click()
# status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
# print(status)

status=driver.find_element(By.XPATH,"//*[@id='q26']/table/tbody/tr[1]/td/label").is_selected()
print(status)
driver.find_element(By.XPATH,"//*[@id='q26']/table/tbody/tr[1]/td/label").click()
status1=driver.find_element(By.XPATH,"//*[@id='q26']/table/tbody/tr[1]/td/label").is_selected()
print(status1)

driver.find_element(By.XPATH,"//*[@id='q15']/table/tbody/tr[1]/td/label").click()
driver.find_element(By.XPATH,"//*[@id='q15']/table/tbody/tr[4]/td/label").click()
driver.find_element(By.XPATH,"//*[@id='q15']/table/tbody/tr[7]/td/label").click()


# select 3 way drop down box
element=driver.find_element_by_id("RESULT_RadioButton-9")
drp=Select(element)

drp.select_by_visible_text("Morning")
# # drp.select_by_index(2)
# drp.select_by_value("Radio-2")

print(len(drp.options)) # drop box e koita option ace show korbe

all_option=drp.options
for x in all_option:
    print(x.text)





