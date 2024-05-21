from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.cookies_page import cookies
from page_objects.common_class import commonClass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re

XE_ICON = (By.CSS_SELECTOR, 'a[aria-label="Home"]')
INSERT_AMOUNT_BOX = (By.CSS_SELECTOR, 'input[id="amount"]')
SOURCE_CURRENCY = (By.CSS_SELECTOR, 'div[id="midmarketFromCurrency"] svg[class="combobox-chevron"]')
DEST_CURRENCY = (By.CSS_SELECTOR, 'div[id="midmarketToCurrency"] svg[class="combobox-chevron"]')
INSERT_SOURCE_CURRENCY = (By.CSS_SELECTOR, 'input[aria-describedby="midmarketFromCurrency-current-selection"]')
INSERT_DST_CURRENCY = (By.CSS_SELECTOR, 'input[aria-describedby="midmarketToCurrency-current-selection"]')
CONVERT_BTN = (By.CSS_SELECTOR, 'button[style*="grid-area:"]')
RESULT_1ST_TEXT = (By.CSS_SELECTOR, 'div[style*="margin-top: 24"] > div > div > p:nth-child(1)')
RESULT_CONV_TEXT = (By.CSS_SELECTOR, 'div[style*="margin-top: 24"] > div > div > p:nth-child(2)')
ORG_X_CONV_RATE = (By.CSS_SELECTOR, 'div[style*="margin-top: 24"] > div > div > div > p:nth-child(1)')
DST_X_CONV_RATE = (By.CSS_SELECTOR, 'div[style*="margin-top: 24"] > div > div > div > p:nth-child(2)')


class convertHomePage(commonClass):
    def __init__(self, driver, config, url, accept_cookies=True) -> None:
        super().__init__(driver, config)
        self.driver.get(url)
        if accept_cookies:
            cookies(self.driver).accept()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(XE_ICON))
        self.insert_amount_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(INSERT_AMOUNT_BOX))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(SOURCE_CURRENCY))
        self.dest_x_dropdown = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(DEST_CURRENCY))
        self.amount = 0

    def insert_amount(self, amount):
        self.insert_amount_box.send_keys(amount)
        self.amount = amount

    def select_src_x(self, currency_name):
        actions = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(INSERT_SOURCE_CURRENCY))
        actions.move_to_element(element).click()
        actions.send_keys(currency_name)
        actions.pause(0.5)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def select_dst_x(self, currency_name):
        actions = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(INSERT_DST_CURRENCY))
        actions.move_to_element(element).click()
        actions.send_keys(currency_name)
        actions.pause(0.5)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def perform_conversion(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(CONVERT_BTN)).click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(CONVERT_BTN))

    def conversion_1st_line(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(RESULT_1ST_TEXT)).text

    def conversion_result(self, amount, currency):
        first_rate = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(ORG_X_CONV_RATE)).text.split(' ')[-2]
        first_rate = float(first_rate.replace(',', '.'))

        line = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(RESULT_CONV_TEXT)).text
        assert re.search(f'^[0-9]+.[0-9]+ {currency}$', line)

        total_conv = int(float(line.split(' ')[0]) * 100)/100
        assert total_conv == int((amount * first_rate) * 100)/100
