import pytest
from page_objects.home_page import convertHomePage

URL = 'https://www.xe.com/'


def test_home_page(webdriver, config):
    convertHomePage(webdriver, config, URL)

def test_convert_real2euros(webdriver, config):
    home_page = convertHomePage(webdriver, config, URL)
    home_page.insert_amount(100)
    home_page.select_src_x('real')
    home_page.select_dst_x('euro')
    home_page.perform_conversion()
    assert home_page.conversion_1st_line() == f'100.00 Brazilian Reais ='
    home_page.conversion_result(100, 'Euros')
