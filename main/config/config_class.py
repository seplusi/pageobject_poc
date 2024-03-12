from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class ConfigInitClass(object):
    def __init__(self) -> None:
        # Load 
        self.config = ConfigParser()
        self.config.read('main/config/config.ini')
        add_args_lst = self.config.get('webdriver', 'options').split('|')
        options = webdriver.ChromeOptions()
        for argument in add_args_lst:
            options.add_argument(argument)
        # Instanciate webdriver
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        
