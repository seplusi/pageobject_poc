import pytest
from page_objects.home_page import convertHomePage
from page_objects.mobile.mobile_home_page import mobileConvertHomePage
from page_objects.mobile.calculator2_page import mobileCalcAppPage


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

def test_webview_mobile_home_page(config, chrome_appiumriver):
    mobileConvertHomePage(chrome_appiumriver, config, URL)

def test_native_app_calc(config, calc_appiumdriver):
    mobileCalcAppPage(calc_appiumdriver, config, explicit_wait=5)