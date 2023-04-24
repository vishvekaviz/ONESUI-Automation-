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
from Pages.Enterpriseadmins.enterpriseadminpage import EnterpriseAdminPage
from Pages.Enterprisestaff.enterprisestaffpage import EnterprisestaffPage
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
 
    def test01_Add_enterprise_staff(self):
        driver = self.driver
       
        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        ES = AccountPage(driver)
        ES.testsearch2_Add_enterprise_staff()
        time.sleep(2)
        print("Add Enterprise Staff")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("logout_successfull")
        time.sleep(2)

    def test02_Login_Enterprisestaff(self):
        driver = self.driver

        ES = EnterprisestaffPage(driver)
        ES.testsearch1_firstlogin()
        time.sleep(2)

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("logout_successfull")
        time.sleep(2)

    def test03_application_page_autorefresh_interval(self):
        driver = self.driver

        ES = EnterprisestaffPage(driver)
        ES.testsearch2_enterprise_login()

        SP = SettingPage(driver)
        SP.testsearch1_auto_refresh_interval_30_second()
        print("30 sec passed")
        SP.testsearch2_auto_refresh_interval_60_second()
        print("06 sec passed")
        SP.testsearch3_auto_refresh_interval_90_second()
        print("90 sec passed")
        SP.testsearch4_auto_refresh_interval_120_second()
        print("120 sec passed")
        SP.testsearch5_application_idle_time_in_3_Minutes()
        SP.testsearch6_application_idle_time_in_2_Minutes()
        print("passed")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("logout_successfull")
        time.sleep(2)

    def test04_inventory_page(self):
        driver = self.driver

        ES = EnterprisestaffPage(driver)
        ES.testsearch2_enterprise_login()

        IP = EnterprisestaffPage(driver)
        IP.testsearch3_inventory_page()
        print("inventory Page Pass")
        time.sleep(2)

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