import pytest
from page_objects.home_page import convertHomePage
from page_objects.mobile.mobile_home_page import mobileConvertHomePage
from page_objects.mobile.calculator2_page import mobileCalcAppPage
import re


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
    home_page = mobileConvertHomePage(chrome_appiumriver, config, URL)

    home_page.insert_amount(100)
    
    home_page.select_src_x('real')
    assert 'real' in home_page.selected_source_currency.text.lower()

    home_page.select_dst_x('euro')
    assert 'euro' in home_page.selected_dst_currency.text.lower()

    home_page.perform_conversion()
    home_page.get_ratings()

    assert home_page.conversion_text1 == "100.00 Brazilian Reais ="

    partial_convertion = round(100*home_page.real2euro, 2)
    re.search(f'{partial_convertion}[0-9]{3} Euros', home_page.conversion_text2)


def test_native_app_calc(config, calc_appiumdriver):
    home_page = mobileCalcAppPage(calc_appiumdriver, config, explicit_wait=5)
    
    home_page.num1.click()
    assert home_page.result_typed.text == '1'
    assert home_page.result_tab.text == ''

    home_page.plus_btn.click()
    assert home_page.result_typed.text == '1+'
    assert home_page.result_tab.text == ''

    home_page.num2.click()
    assert home_page.result_typed.text == '1+2'
    assert home_page.result_tab.text == '3'

    home_page.equal_btn.click()
    assert home_page.result_typed.text == '3'
    assert home_page.result_tab.text == ''
