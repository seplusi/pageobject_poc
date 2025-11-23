from page_objects.common_class import commonClass
from selenium.webdriver.support import expected_conditions as EC


class mobileSelectChromeAccPage(commonClass):
    def __init__(self, driver, config, explicit_wait=20):
        super().__init__(driver, config, __class__.__name__, explicit_wait)
        self.use_acc_btn = self.wait_driver.until(EC.visibility_of_element_located(self.locators['USE_ACC_BTN']))
        self.without_acc_btn = self.wait_driver.until(EC.visibility_of_element_located(self.locators['WITHOUT_ACC_BTN']))

    def use_without_acc(self):
        self.without_acc_btn.click()

    