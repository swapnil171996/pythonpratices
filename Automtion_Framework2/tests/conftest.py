import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

# cmd to run through commandline python -m pytest -v --browser=chrome .\tests\test_dummy_website.py
# python -m pytest -v --browser=chrome --headless=False .\tests\test_dummy_website.py

@pytest.fixture(scope="class")
def get_driver(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://sqatools.in/dummy-booking-website/")
    request.cls.driver=driver
    yield
    driver.close()

from base.webdriver_factory import WebdriverFactory

def pytest_addoption(parser):
    parser.addoption("--browser",action='store',default=None,help='browser to launch')
    parser.addoption("--headless",action='store',default=None,help='GUI to launch')
'''@pytest.fixture(scope="class")
def get_driver_with_option(request):
    wf=WebdriverFactory(browser='chrome',headless=False)
    driver=wf.get_driver_instance()
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()'''


@pytest.fixture(scope="class")
def get_driver_with_option(request,pytestconfig):
    browser=pytestconfig.getoption("browser")
    headless=pytestconfig.getoption("headless")
    wf = WebdriverFactory(browser=browser, headless=headless)
    driver = wf.get_driver_instance()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()




