import HtmlTestRunner
from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"...","..."))
# we will import Loginpage and Homepage class to access its all function
from POMproject.pages.loginPages import LoginPage
from POMproject.pages.homePage import HomePage



class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(
            executable_path='C:\\Users\\Mahid Ahmed\\PycharmProjects\\seleniumscripts\\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver=self.driver

        self.driver.get('https://opensource-demo.orangehrmlive.com')

        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print('Successfully completed')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Mahid Ahmed\\PycharmProjects\\seleniumscripts\\reports"))

