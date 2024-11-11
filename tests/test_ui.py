import pytest
from page_objects.home_page import convertHomePage
from page_objects.mobile.mobile_home_page import mobileConvertHomePage

URL = 'https://www.xe.com/'


def test_home_page(webdriver, config):
    convertHomePage(webdriver, config, URL, accept_cookies=False)

def test_convert_real2euros(webdriver, config):
    home_page = convertHomePage(webdriver, config, URL, accept_cookies=False)
    home_page.insert_amount(100)
    home_page.select_src_x('real')
    home_page.select_dst_x('euro')
    home_page.perform_conversion()
    assert home_page.conversion_1st_line() == f'100.00 Brazilian Reais ='
    home_page.conversion_result(100, 'Euros')

def test_mobile_home_page(appiumdriver, config):
    home_page = mobileConvertHomePage(appiumdriver, config, URL)
