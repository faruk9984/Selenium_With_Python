"""
# =======================================================
# Selenium with Python Tutorial 27-Working with Cookies

from selenium import webdriver

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()

cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

cookie={'name':'Mycookie','value':'1234567890'}
driver.add_cookie(cookie)

cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

driver.delete_cookie('Mycookie')

cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))



# =======================================================
# Selenium with Python Tutorial 28-Capture Screenshots

from selenium import webdriver

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.w3schools.com/")
driver.maximize_window()

driver.save_screenshot("C:/Users/aslam/Desktop/New folder/home.jpg")
driver.get_screenshot_as_file("C:/Users/aslam/Desktop/New folder/home1.png")



# =======================================================
# Selenium with Python Tutorial 29-Logging | Generate log file

import logging

logging.basicConfig(filename="S:/Python Programming/Amulyas Academy/seleniumlog/test2.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%y %I:%M:%S: %p',
                    level=logging.DEBUG)


logging.debug("this is debug message")
logging.info("this is info message")
logging.warning("this is warning message")
logging.error('this is error message')
logging.critical("this is critical message")

# another way you can do that-->best way

import logging

logging.basicConfig(filename="S:/Python Programming/Amulyas Academy/seleniumlog/test2.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%y %I:%M:%S: %p')

loger=logging.getLogger()
loger.setLevel(logging.DEBUG)

loger.debug("this is debug message")
loger.info("this is info message")
loger.warning("this is warning message")
loger.error('this is error message')
loger.critical("this is critical message")


# =======================================================
# Selenium with Python Tutorial 30-Python UnitTest Framework

import unittest

class Test(unittest.TestCase):
    def test_firstTest(self):
        print("this is my first unit test case")

if __name__ == '__main__':
    unittest.main()


# another way unittest framework--> best

import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_google(self):
        self.driver=webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("title "+self.driver.title)
        print(self.driver.current_url)
        self.driver.close()

    def test_bing(self):
        self.driver=webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get("https://bing.com")
        print("title: "+self.driver.title)
        print(self.driver.current_url)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()



# ===============================================================
# Selenium with Python Tutorial 31-Python UnitTest Framework Methods

import unittest

def setUpModule():
    print("setUpModule")

def tearDownModule():
    print('tearDownModule')

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("this is login test")

    @classmethod
    def tearDown(self):
        print("this is logout test")

    @classmethod
    def setUpClass(cls):
        print("open application")

    @classmethod
    def tearDownClass(cls):
        print("close application")

    def test_search(self):
        print("this is search test")

    def test_advancedsearch(self):
        print("this is advancedsearch test")

    def test_prepaidRecharge(self):
        print("this is prepaidRecharge test")

    def test_postpaidRecharge(self):
        print("this is postpaidRecharge test")

if __name__ == '__main__':
    unittest.main()



# ===========================================================
# Selenium with Python Tutorial 32-Python UnitTest | Skipping Tests


import unittest


class AppTesting(unittest.TestCase):
    @unittest.SkipTest
    def test_search(self):
        print("this is search test")

    @unittest.skip("i am skipping because of it is not yet ready")
    def test_advancedsearch(self):
        print("this is advancedsearch test")

    @unittest.skipIf(1==1,"one is equal is one")
    def test_prepaidRecharge(self):
        print("this is prepaidRecharge test")

    def test_postpaidRecharge(self):
        print("this is postpaidRecharge test")

    def test_logingmail(self):
        print('this is login by mail')

    def test_loginbytwitter(self):
        print('this is login by twitter')

if __name__ == '__main__':
    unittest.main()




# =================================================================
# Selenium with Python Tutorial 33-Python UnitTest|Assertions|assertEqual & assertNotEqual


import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("https://www.google.com/")
        # print(driver.title)
        titleofpage=driver.title

        self.assertEqual("Google1",titleofpage,"title is not same")
        # self.assertNotEqual("Google123",titleofpage)


if __name__ == '__main__':
    unittest.main()





# ============================================================
# Selenium with Python Tutorial 34-Python UnitTest|Assertions|assertTrue & assertFalse


import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("https://www.google.com/")
        # print(driver.title)
        titleofpage=driver.title

        self.assertTrue(titleofpage=='Google')
        # self.assertFalse(titleofpage == 'Google')


if __name__ == '__main__':
    unittest.main()



# ============================================================
# Selenium with Python Tutorial 35-Python UnitTest|Assertions|assertIsNone & assertIsNotNone

import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="chromedriver.exe")
        # driver=None
        self.assertIsNone(driver)
        # self.assertIsNotNone(driver)




if __name__ == '__main__':
    unittest.main()



# ============================================================
# Selenium with Python Tutorial 36-Python UnitTest|Assertions|assertIn & assertNotIn


import unittest

class Test(unittest.TestCase):
    def testname(self):
        list=['python','selenium','java']
        self.assertIn('python',list)
        # self.assertNotIn("ruby",list)
    def testname1(self):
        list=['python','selenium','java']
        self.assertIn('python',list)
        # self.assertNotIn("ruby",list)


if __name__ == '__main__':
    unittest.main()



# ============================================================
# Selenium with Python Tutorial 37-Python UnitTest|Assertions|Relational comparison


import unittest

class Test(unittest.TestCase):
    def testname(self):
        self.assertGreater(100,10)
        # self.assertGreater(10,100)

        # self.assertGreaterEqual(101,1011)

        # self.assertLess(5,10)

        # self.assertLessEqual(5,5)


if __name__ == '__main__':
    unittest.main()


# ============================================================
# Selenium with Python Tutorial 38-Python UnitTest |Creating and Running Test Suites | Batch Testing

# PACKAGE1
# package2
# testsuite




# =================================================
# Selenium with Python Tutorial 39-PyTest | Installation and Getting Started
# run korte hobe terminal e -->pytest -v -s /pytest -v -s selenium11.py

import pytest

def testMethod():
    print('this is test method 1')

def testMethod2():
    print('this is test method 2')






# =========================================================================
# Selenium with Python Tutorial 40-PyTest | Working with PyTest Fixtures
import pytest


@pytest.fixture()
def setup():
    print('once before every method')


def testmethod1(setup):
    print('this is test method 1')


def testmethod2(setup):
    print('this is test method 2')

# DEMO 2



import pytest

@pytest.yield_fixture()
def setup():
    print('once before every method')
    yield
    print('once after every method')

def testmethod1(setup):
    print('this is test method 1')

def testmethod2(setup):
    print('this is test method 2')




# ========================================================================
# Selenium with Python Tutorial 41-PyTest | Run Multiple Tests in PyTest

# mypack e ace sob



# ========================================================================
# Selenium with Python | Unittest+ HTML Reports + Page Object Model

# selenium python test case using unit test,html report
# run korte hobe terminal e -->python selenium10.py
# report genarate hobe reports folder e

from selenium import webdriver
import unittest
import HtmlTestRunner

class OrangeHRMTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="chromedriver.exe")
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM",self.driver.title,"webpage title is not matching")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM",self.driver.title,"webpage does not match")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("test completed.....")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='S:/Python Programming/Amulyas Academy/Reports'))
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..//Reports'))



# selenium python project unit test ,pom,html report


# ========================================================================
# Selenium with Python | Oracle Database Connectivity using cx_Oracle |Data Driven Testing
# Selenium with Python | PyTest HTML Report Generation | pytest-html module

from selenium import webdriver
import pytest

class TestOrangeHRM():
    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homepagehtml(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        assert self.driver.title=="OrangeHRM"

    def test_login(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title=="OrangeHRM"


"""
# =================================================================
# How To Generate Allure Reports in Selenium with Python & PyTest

