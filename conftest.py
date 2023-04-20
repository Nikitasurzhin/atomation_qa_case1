import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()
