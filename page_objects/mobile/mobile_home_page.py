from page_objects.common_class import commonClass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time


class mobileConvertHomePage(commonClass):
    def __init__(self, driver, config, url, explicit_wait=20) -> None:
        super().__init__(driver, config, __class__.__name__, explicit_wait)
        self.driver.get(url)

        self.wait_driver.until(EC.visibility_of_element_located(self.locators['DOLLAR_SIGN']))
        assert self.wait_driver.until(EC.visibility_of_element_located(self.locators['CONVERT_TAB'])).tag_name == 'Convert'
        assert self.wait_driver.until(EC.visibility_of_element_located(self.locators['SEND_TAB'])).tag_name == 'Send'
        assert self.wait_driver.until(EC.visibility_of_element_located(self.locators['CHARTS_TAB'])).tag_name == 'Charts'
        alerts_tab = self.wait_driver.until(EC.visibility_of_element_located(self.locators['ALERTS_TAB']))
        assert alerts_tab.tag_name == 'Alerts'
        assert self.wait_driver.until(EC.visibility_of_element_located(self.locators['AMOUNT_TXT'])).text == 'Amount'
        assert self.wait_driver.until(EC.visibility_of_element_located(self.locators['AMOUNT'])).tag_name == '1.00'
