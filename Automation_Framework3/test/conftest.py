import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def get_driver(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.booking.com/flights/index.html?aid=304142&label=gen173nr-10CAEoggI46AdIM1gEaGyIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4Ar_808oGwAIB0gIkZWNhNTA0N2ItMzFhMy00MzJiLTk5NjQtMzJmZTg3M2IwMGE32AIB4AIB&sid=68d39a0ab13105dddeeaab6c90e91fce&from=booking&")
    request.cls.driver=driver
    yield
    driver.close()