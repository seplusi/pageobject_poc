import pytest
from resources.config.config_class import ConfigInitClass

@pytest.fixture(scope="function", name="init_config_object")
def init_config_object_create():
    return ConfigInitClass()

@pytest.fixture(scope="function", name="webdriver")
def webdriver_create(init_config_object):
    init_config_object.webdriver()
    yield init_config_object.driver
    
    # Destroying webdriver"
    init_config_object.driver.stop_client()
    init_config_object.driver.close()

@pytest.fixture(scope="function", name="config")
def config_fixture(init_config_object):
    return init_config_object.config

@pytest.fixture(scope="function", name="appiumdriver")
def appiumdriver_create(init_config_object):
    init_config_object.appiumdriver()
    yield init_config_object.appiumdriver

    init_config_object.appiumdriver.quit()
    