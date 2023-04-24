from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import HtmlTestRunner
import sys
sys.path.append('C:\\Users\\vishv\\Desktop\\ones1.2')

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Pages.accountpage import AccountPage

from Pages.Vendorstaff.vendorstaffpage import VendorStaffPage
from Pages.settingPage.application import SettingPage
from Pages.configurationPage import ConfigPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(options=options, executable_path="C:\\Users\\vishv\\Desktop\\ones1.2\\Drivers\\chromedriver.exe")
        cls.driver.get("https://192.168.74.133")
        cls.driver.maximize_window()
 
    def test01_Add_Vendor_staff(self):
        driver = self.driver
       
        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        vs = AccountPage(driver)
        vs.testsearch3_Add_vendor_staff()
        time.sleep(2)
        print("vendor staff add successfull")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("logout_successfull")
        time.sleep(2)

    def test02_Login_vendor_staff(self):
        driver = self.driver

        vs = VendorStaffPage(driver)
        vs.testsearch1_firstlogin()
        time.sleep(2)

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("logout_successfull")
        time.sleep(2)

    def test03_application_page_autorefresh_interval(self):
        driver = self.driver

        vs = VendorStaffPage(driver)
        vs.testsearch2_vendor_login()

        SP = SettingPage(driver)
        SP.testsearch1_auto_refresh_interval_30_second()
        print("30 sec passed")
        SP.testsearch2_auto_refresh_interval_60_second()
        print("06 sec passed")
        SP.testsearch3_auto_refresh_interval_90_second()
        print("90 sec passed")
        SP.testsearch4_auto_refresh_interval_120_second()
        print("120 sec passed")
        print("passed")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("logout_successfull")
        time.sleep(2)

    def test04_inventory_page(self):
        driver = self.driver

        vs = VendorStaffPage(driver)
        vs.testsearch2_vendor_login()

        IP = VendorStaffPage(driver)
        IP.testsearch3_inventory_page()
        print("inventory Page Pass")
        time.sleep(2)

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("logout_successfull")
        time.sleep(2)

    def test05_ConfigurationPAge(self):
        driver = self.driver

        EA = VendorStaffPage(driver)
        EA.testsearch2_vendor_login()

        CP = ConfigPage(driver)
        CP.testsearch1()
        print("config page passed")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("logout_successfull")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\vishv\\Desktop\\ones1.2\\reports'))