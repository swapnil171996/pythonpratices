import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture(scope="class")
def get_driver(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    request.cls.driver=driver
    yield
    driver.close()
