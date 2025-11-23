from page_objects.common_class import commonClass
from selenium.webdriver.support import expected_conditions as EC


class mobileSelectPrivacyPage(commonClass):
    def __init__(self, driver, config, explicit_wait=10):
        super().__init__(driver, config, __class__.__name__, explicit_wait)
        self.acc_btn = self.wait_driver.until(EC.visibility_of_element_located(self.locators['ACC_BTN']))
        self.settings_btn = self.wait_driver.until(EC.visibility_of_element_located(self.locators['SETTINGS_BTN']))

    def accept_default_privacy(self):
        self.acc_btn.click()
