import json
from configparser import ConfigParser
from selenium import webdriver
from appium import webdriver as appiumdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.mobile.choose_chrome_accounts import mobileSelectChromeAccPage
from page_objects.mobile.mobile_select_privacy import mobileSelectPrivacyPage
import time


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

    def appiumdriver(self, extra_caps=None):
        options = UiAutomator2Options()
        # Instanciate appiumdriver
        appium_capabilities = json.loads(self.config.get('appiumdriver', 'default_capabilities'))
        if extra_caps:
            extra_appium_caps = json.loads(self.config.get('appiumdriver', f'{extra_caps}_capabilities'))
            appium_capabilities.update(extra_appium_caps)
        options.load_capabilities(appium_capabilities)
        appium_server_url = self.config.get('appiumdriver', 'appium_server_url')
        self.appiumdriver = appiumdriver.Remote(appium_server_url, options=options)

    def switch_2_context(self, context_name):
        for _ in range(10):
            if context_name in self.appiumdriver.contexts:
                break
            time.sleep(1)
        self.appiumdriver.switch_to.context(context_name)
    
    def use_without_acc(self):
        mobileSelectChromeAccPage(self.appiumdriver, self.config).use_without_acc()

    def accept_privacy(self):
        mobileSelectPrivacyPage(self.appiumdriver, self.config).accept_default_privacy()
