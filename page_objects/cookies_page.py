from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.common_class import commonClass


class cookies(commonClass):
    def __init__(self, driver, config) -> None:
        super().__init__(driver, config)
        self.locators = self.get_all_locators(__class__.__name__)
        self.accept_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(self.locators['ACCEPT_BUTTON']))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(self.locators['CUSTOMIZE_BUTTON']))
    
    def accept(self):
        self.accept_btn.click()
