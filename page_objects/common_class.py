import time
from selenium.webdriver.common.by import By


class commonClass(object):
    def __init__(self, driver, config, page_obj_class_name) -> None:
        self.driver = driver
        self.config = config
        # Load page specific locators 
        self.config.read(f'resources/locator/{page_obj_class_name}.ini')
        self.locators = self._get_all_locators(page_obj_class_name)

    def _get_all_locators(self, section_name):
        locators = {}
        for key in self.config[section_name]:
            type, selector = self.config[section_name][key].split(', ')
            locators[key.upper()] = (eval(f'By.{type}'), selector)
        
        return locators
    
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
