import pytest

URL = 'https://www.alten.es'


def test_home_page(webdriver, config):
    webdriver.get(URL)
    print("dfbfbdfb")