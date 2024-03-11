import pytest

URL = 'https://www.alten.es'


def test_home_page(webdriver):
    webdriver.get(URL)
    print("dfbfbdfb")