import json
from configparser import ConfigParser
from selenium import webdriver
from appium import webdriver as appiumdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait


class ConfigInitClass(object):
    def __init__(self) -> None:
        # Load 
        self.config = ConfigParser()
        self.config.read('resources/config/config.ini')
        add_args_lst = self.config.get('webdriver', 'options').split('|')
        self.options = webdriver.ChromeOptions()
        for argument in add_args_lst:
            self.options.add_argument(argument)

    def webdriver(self, explicit_wait=10):
        # Instanciate webdriver
        self.driver = webdriver.Chrome(options=self.options, service=ChromeService(ChromeDriverManager().install()))

    def appiumdriver(self):
        options = UiAutomator2Options()
        # Instanciate appiumdriver
        appium_capabilities = json.loads(self.config.get('appiumdriver', 'capabilities'))
        options.load_capabilities(appium_capabilities)
        appium_server_url = self.config.get('appiumdriver', 'appium_server_url')
        self.appiumdriver = appiumdriver.Remote(appium_server_url, options=options)
