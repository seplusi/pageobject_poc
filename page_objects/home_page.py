from selenium.webdriver.support import expected_conditions as EC
from page_objects.cookies_page import cookies
from page_objects.common_class import commonClass
from selenium.webdriver.common.keys import Keys
import re
import time
from selenium.common.exceptions import StaleElementReferenceException


class convertHomePage(commonClass):
    def __init__(self, driver, config, url, accept_cookies=True, explicit_wait=20) -> None:
        super().__init__(driver, config, __class__.__name__, explicit_wait)
        self.driver.get(url)
        if accept_cookies:
            cookies(self.driver, config).accept()
        self.wait_driver.until(EC.element_to_be_clickable(self.locators['XE_ICON']))
        self.insert_amount_box = self.wait_driver.until(EC.element_to_be_clickable(self.locators['INSERT_AMOUNT_BOX']))
        self.wait_driver.until(EC.element_to_be_clickable(self.locators['SOURCE_CURRENCY']))
        self.dest_x_dropdown = self.wait_driver.until(EC.element_to_be_clickable(self.locators['DEST_CURRENCY']))
        self.amount = 0

    def insert_amount(self, amount):
        self.insert_amount_box.send_keys(amount)
        self.amount = amount

    def select_src_x(self, currency_name):
        # Click textbox and write currency name
        element = self.wait_driver.until(EC.visibility_of_element_located(self.locators['INSERT_SOURCE_CURRENCY']))
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

    def conversion_1st_line(self):
        return self.wait_driver.until(EC.visibility_of_element_located(self.locators['RESULT_1ST_TEXT'])).text

    def conversion_result(self, amount, currency):
        first_rate = self.wait_driver.until(EC.visibility_of_element_located(self.locators['ORG_X_CONV_RATE'])).text.split(' ')[-2]
        first_rate = float(first_rate.replace(',', '.'))

        line = self.wait_driver.until(EC.visibility_of_element_located(self.locators['RESULT_CONV_TEXT'])).text
        assert re.search(f'^[0-9]+.[0-9]+ {currency}$', line)

        total_conv = int(float(line.split(' ')[0]) * 100)/100
        assert total_conv == int((amount * first_rate) * 100)/100
