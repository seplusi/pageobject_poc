from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.cookies_page import cookies
from page_objects.common_class import commonClass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re


class convertHomePage(commonClass):
    def __init__(self, driver, config, url, accept_cookies=True) -> None:
        super().__init__(driver, config, __class__.__name__)
        self.driver.get(url)
        if accept_cookies:
            cookies(self.driver, config).accept()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(self.locators['XE_ICON']))
        self.insert_amount_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(self.locators['INSERT_AMOUNT_BOX']))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(self.locators['SOURCE_CURRENCY']))
        self.dest_x_dropdown = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(self.locators['DEST_CURRENCY']))
        self.amount = 0

    def insert_amount(self, amount):
        self.insert_amount_box.send_keys(amount)
        self.amount = amount

    def select_src_x(self, currency_name):
        actions = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators['INSERT_SOURCE_CURRENCY']))
        actions.move_to_element(element).click()
        actions.send_keys(currency_name)
        actions.pause(0.5)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def select_dst_x(self, currency_name):
        actions = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators['INSERT_DST_CURRENCY']))
        actions.move_to_element(element).click()
        actions.send_keys(currency_name)
        actions.pause(0.5)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def perform_conversion(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.locators['CONVERT_BTN'])).click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(self.locators['CONVERT_BTN']))

    def conversion_1st_line(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators['RESULT_1ST_TEXT'])).text

    def conversion_result(self, amount, currency):
        first_rate = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators['ORG_X_CONV_RATE'])).text.split(' ')[-2]
        first_rate = float(first_rate.replace(',', '.'))

        line = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators['RESULT_CONV_TEXT'])).text
        assert re.search(f'^[0-9]+.[0-9]+ {currency}$', line)

        total_conv = int(float(line.split(' ')[0]) * 100)/100
        assert total_conv == int((amount * first_rate) * 100)/100
