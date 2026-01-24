import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def get_driver(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://sqatools.in/dummy-booking-website/")
    request.cls.var1=driver #hold value of var1 in driver variable for any class
    yield
    driver.close()


