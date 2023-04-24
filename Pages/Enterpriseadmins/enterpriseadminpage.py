from selenium.webdriver.common.by import By
import time

class EnterpriseAdminPage:

    def __init__(self, driver):
        self.driver = driver

    def testsearch1_firstlogin(self):
        driver = self.driver
        driver.find_element("id", "username").send_keys("vishu")
        driver.find_element("id", "password").send_keys("aviz@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Admin@123")
        driver.find_element(By.XPATH, "//input[@id='confirmpassword']").send_keys("Admin@123")
        driver.find_element(By.XPATH, "//button[text()='Reset password']").click()
        time.sleep(3)
        driver.find_element("id", "username").send_keys("vishu")
        driver.find_element("id", "password").send_keys("Admin@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

    def testsearch2_enterprise_login(self):
        driver = self.driver
        driver.find_element("id", "username").send_keys("vishu")
        driver.find_element("id", "password").send_keys("Admin@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)


    def testsearch3_inventory_page(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//img[@alt='Inventory Icon']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@class='PrivateSwitchBase-input css-1m9pwf3'][@type='checkbox'][@aria-label='Select all rows']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[text()='Custom Upgrade']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[text()='Reboot Devices']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@type='checkbox'][@aria-label='Unselect all rows']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//p[text()='Add/Remove Devices']").click()
        time.sleep(2)        
        driver.find_element(By.XPATH, "//p[text()='Download YAML']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[text()='Add/Remove Devices']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Save & Apply']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@src='/static/media/NewAvatar.9ac40ba1.svg']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//li[@tabindex='-1']").click()
        time.sleep(2)







