from page_objects.common_class import commonClass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException


class mobileConvertHomePage(commonClass):
    def __init__(self, driver, config, url, explicit_wait=20) -> None:
        super().__init__(driver, config, __class__.__name__, explicit_wait)
        self.driver.get(url)

        self.wait_driver.until(EC.visibility_of_element_located(self.locators['DOLLAR_SIGN']))
        assert self.wait_driver.until(EC.visibility_of_element_located(self.locators['CONVERT_TAB'])).text == 'Convert'
        assert self.wait_driver.until(EC.visibility_of_element_located(self.locators['SEND_TAB'])).text == 'Send'
        assert self.wait_driver.until(EC.visibility_of_element_located(self.locators['CHARTS_TAB'])).text == 'Charts'
        alerts_tab = self.wait_driver.until(EC.visibility_of_element_located(self.locators['ALERTS_TAB']))
        assert alerts_tab.text == 'Alerts'
        assert self.wait_driver.until(EC.visibility_of_element_located(self.locators['AMOUNT_TXT'])).text == 'Amount'
        self.insert_amount_box = self.wait_driver.until(EC.visibility_of_element_located(self.locators['AMOUNT']))
        # Accept cookie
        self.wait_driver.until(EC.visibility_of_element_located(self.locators['ACCEPT_COOKIE'])).click()

    def insert_amount(self, amount):
        self.insert_amount_box.send_keys(Keys.BACKSPACE)
        self.insert_amount_box.send_keys(amount)
        self.amount = amount

    def select_src_x(self, currency_name):
        # Click textbox and write currency name
        element = self.wait_driver.until(EC.visibility_of_element_located(self.locators['SOURCE_CURRENCY']))
        element.click()
        element.send_keys(currency_name)
        for _ in range(10):
            try:
                time.sleep(0.1)
                # Wait for 1st element in list to be our currency
                self.wait_driver.until(EC.visibility_of_element_located(self.locators['INSERT_SOURCE_CURRENCY_LST']))
                currency = self.wait_driver.until(EC.visibility_of_element_located(self.locators['FIRST_CURRENCY']))
                if currency_name.lower() in currency.text.lower():
                    currency.click()
                    break
            except StaleElementReferenceException:
                continue
        else:
            assert False, f'Currency {currency_name} not found.'
        # Press enter to finish selection
        element.send_keys(Keys.ENTER)

    def select_dst_x(self, currency_name):
        # Click textbox and write currency name
        element = self.wait_driver.until(EC.visibility_of_element_located(self.locators['INSERT_DST_CURRENCY']))
        element.click()
        element.send_keys(currency_name)
        for _ in range(10):
            try:
                time.sleep(0.1)
                # Wait for 1st element in list to be our currency
                self.wait_driver.until(EC.visibility_of_element_located(self.locators['INSERT_DST_CURRENCY_LST']))
                currency = self.wait_driver.until(EC.visibility_of_element_located(self.locators['FIRST_DST_CURRENCY']))
                if currency_name.lower() in currency.text.lower():
                    currency.click()
                    break
            except StaleElementReferenceException:
                continue
        else:
            assert False, f'Currency {currency_name} not found.'
        # Press enter to finish selection
        element.send_keys(Keys.ENTER)

    def perform_conversion(self):
        self.wait_driver.until(EC.element_to_be_clickable(self.locators['CONVERT_BTN'])).click()
        self.wait_driver.until(EC.invisibility_of_element_located(self.locators['CONVERT_BTN']))