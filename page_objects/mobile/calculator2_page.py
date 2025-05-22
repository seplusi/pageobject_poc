from page_objects.common_class import commonClass
from selenium.webdriver.support import expected_conditions as EC


class mobileCalcAppPage(commonClass):
    def __init__(self, driver, config, explicit_wait=20) -> None:
        super().__init__(driver, config, __class__.__name__, explicit_wait)
        
        self.equal_btn = self.wait_driver.until(EC.visibility_of_element_located(self.locators['EQUAL_BTN']))
        self.plus_btn = self.wait_driver.until(EC.visibility_of_element_located(self.locators['PLUS_BN']))
        self.wait_driver.until(EC.visibility_of_element_located(self.locators['MINUS_BN']))
        self.wait_driver.until(EC.visibility_of_element_located(self.locators['MULTPLY_BN']))
        self.wait_driver.until(EC.visibility_of_element_located(self.locators['DIV_BN']))
        self.wait_driver.until(EC.visibility_of_element_located(self.locators['DEL_BN']))
        self.wait_driver.until(EC.visibility_of_element_located(self.locators['CLR_BN']))
        self.wait_driver.until(EC.visibility_of_element_located(self.locators['PERCNT_BN']))
        self.wait_driver.until(EC.visibility_of_element_located(self.locators['DECIMAL_BN']))
        self.num1 = self.wait_driver.until(EC.visibility_of_element_located(self.locators['DIGIT1']))
        self.num1 = self.wait_driver.until(EC.visibility_of_element_located(self.locators['DIGIT1']))
        self.num2 = self.wait_driver.until(EC.visibility_of_element_located(self.locators['DIGIT2']))
        self.num3 = self.wait_driver.until(EC.visibility_of_element_located(self.locators['DIGIT3']))
        self.num4 = self.wait_driver.until(EC.visibility_of_element_located(self.locators['DIGIT4']))
        self.num5 = self.wait_driver.until(EC.visibility_of_element_located(self.locators['DIGIT5']))
        self.num6 = self.wait_driver.until(EC.visibility_of_element_located(self.locators['DIGIT6']))
        self.num7 = self.wait_driver.until(EC.visibility_of_element_located(self.locators['DIGIT7']))
        self.num8 = self.wait_driver.until(EC.visibility_of_element_located(self.locators['DIGIT8']))
        self.num9 = self.wait_driver.until(EC.visibility_of_element_located(self.locators['DIGIT9']))

    @property
    def result_typed(self):
        return self.wait_driver.until(EC.visibility_of_element_located(self.locators['TYPED_FORMULA']))

    @property
    def result_tab(self):
        return self.wait_driver.until(EC.visibility_of_element_located(self.locators['RESULT']))

    def expected_typed(self, value):
        assert self.result_typed.text == value
        