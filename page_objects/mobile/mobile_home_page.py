from page_objects.common_class import commonClass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class mobileConvertHomePage(commonClass):
    def __init__(self, driver, config, url, explicit_wait=20) -> None:
        super().__init__(driver, config, __class__.__name__, explicit_wait)
        self.driver.get(url)
        self.wait_driver.until(EC.visibility_of_element_located(self.locators['DOLLAR_SIGN']))
        self.wait_driver.until(EC.visibility_of_element_located(self.locators['CONVERT_TAB']))
        self.wait_driver.until(EC.visibility_of_element_located(self.locators['SEND_TAB']))
