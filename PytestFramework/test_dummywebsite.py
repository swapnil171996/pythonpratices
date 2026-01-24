import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:

    def test_enter_passenger_details(self):
        self.var1.find_element(By.XPATH,'(//input[@name="firstname"])[1]').send_keys("kishor")
        self.var1.find_element(By.XPATH,'(//input[@name="firstname"])[2]').send_keys("patil")
        self.var1.find_element(By.ID,"birthday").send_keys("04/06/1990")
        self.var1.find_element(By.ID,"male").click()
        time.sleep(10)

    def test_enter_travel_details(self):
        drop_element=self.var1.find_element(By.ID,'admorepass')
        dropdown=Select(drop_element)
        dropdown.select_by_value("2")

        self.var1.find_element(By.ID,"oneway").click()
        self.var1.find_element(By.ID,"fromcity").send_keys("Mumbai")
        self.var1.find_element(By.ID, "destcity").send_keys("Pune")
        self.var1.find_element(By.ID,"departdate").send_keys("04/12/2025")
        self.var1.find_element(By.ID,"returndate").send_keys("05/12/2025")
        time.sleep(10)