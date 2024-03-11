import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function", name="webdriver")
def webdriver_create():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Instanciate webdriver
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    yield driver
    # Destroying webdriver"
    driver.stop_client()
    driver.close()

@pytest.fixture
def order():
    return []

@pytest.fixture
def top(order, innermost):
    order.append("top")