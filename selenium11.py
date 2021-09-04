# =================================================================
# How To Generate Allure Reports in Selenium with Python & PyTest


import pytest
import allure
from selenium import webdriver
from allure_commons.types import AttachmentType

@allure.severity(allure.severity_level.NORMAL)
class TestHRM:
    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        # self.driver=webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver=webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        status=self.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
        if status==True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployess(self):
        pytest.skip("skipping test..later i will implement")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        # self.driver=webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver=webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        
        act_title=self.driver.title
        if act_title=="OrangeHRM123":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="testLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False



