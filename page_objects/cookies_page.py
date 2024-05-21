from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ACCEPT_BUTTON = (By.CSS_SELECTOR, 'section[class] div[style*="display: flex; justify"] > button:nth-of-type(2)')
CUSTOMIZE_BUTTON = (By.CSS_SELECTOR, 'section[class] div[style*="display: flex; justify"] > button:nth-of-type(1)')


class cookies(object):
    def __init__(self, driver) -> None:
        self.accept_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(ACCEPT_BUTTON))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(CUSTOMIZE_BUTTON))
    
    def accept(self):
        self.accept_btn.click()
