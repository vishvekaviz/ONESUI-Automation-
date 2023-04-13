import unittest
import time
import pytest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import os
from selenium.webdriver.common.action_chains import ActionChains


class SeleniumTest(unittest.TestCase):

# url and credential login 
    @classmethod
    def setUp(self):
        # self.driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        driver = self.driver
        driver.get("https://192.168.74.129")  


    def testsearch1_profile_change_firstname_lastname(self):
        driver = self.driver
        driver.find_element("id", "username").send_keys("superadmin")
        driver.find_element("id", "password").send_keys("Admin@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@aria-label='Profile']//img[@src='/static/media/NewAvatar.9ac40ba1.svg']").click()
        driver.find_element(By.XPATH, "//li[text()='Profile']").click()
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(Keys.CONTROL, 'a')
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("vishu")
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys(Keys.CONTROL, 'a')
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("sharma")
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(4)
        valid_message = driver.find_element(By.XPATH, "//div[text()='Users Updated Successfully']")
        if valid_message:
            print("", valid_message.text)
        else:
            print("user not updated")

        driver.find_element(By.XPATH, "//div[@aria-label='Profile']//img[@src='/static/media/NewAvatar.9ac40ba1.svg']").click()
        driver.find_element(By.XPATH, "//li[text()='Profile']").click()
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(Keys.CONTROL, 'a')
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("superadmin")
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys(Keys.CONTROL, 'a')
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("aviz")
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(4)
        valid_message = driver.find_element(By.XPATH, "//div[text()='Users Updated Successfully']")
        if valid_message:
            print("", valid_message.text)
        else:
            print("user not updated")




    @classmethod
    def tearDown(self):
        self.driver.close()


if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\vishv\\Desktop\\ones1.2\\reports'))

