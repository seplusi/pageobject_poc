import time
from selenium.webdriver.common.by import By


class commonClass(object):
    def __init__(self, driver, config) -> None:
        self.driver = driver
        self.config = config
    
    def wait_4_element_visible(self, locator, timeout=10):
        initial_ts = int(time.time())
        exception = None
        while int(time.time()) < initial_ts + timeout:
            try:
                if self.driver.find_element(*locator).is_displayed():
                    break
            except Exception as e:
                exception = e
        else:
            raise exception if exception else TimeoutError
