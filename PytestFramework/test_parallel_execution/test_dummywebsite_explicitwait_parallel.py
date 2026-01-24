import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locator_findss import *
from resource_datas import *
#pip install -xdist

@pytest.mark.usefixtures("get_driver")
@pytest.mark.parametrize("firstname,lastname,dob",[("john","Pole","09/05/1990"),("ram","Patil","12/06/1997")])
class TestDummyWebsite:
    @pytest.fixture(autouse=True)
    def setup(self,firstname,lastname,dob):
        self.firstname=firstname
        self.lastname=lastname
        self.dob=dob

    def get_element(self,locator):
        wait=WebDriverWait(self.var1,timeout=20)
        return wait.until(ec.presence_of_element_located(locator))
    def test_enter_passenger_details(self):
        self.get_element(first_name_element).send_keys(self.firstname)
        self.get_element(last_name_element).send_keys(self.lastname)

    def test_enter_dob(self):
        self.get_element(dob_calender).send_keys(self.dob)

    def test_select_male_radio(self):
        self.get_element(male_radio_btn).click()
        time.sleep(10)

    def test_enter_travel_details(self):
        drop_element=self.get_element(add_more_pass_dd)
        dropdown=Select(drop_element)
        dropdown.select_by_value("2")

    def test_select_trip_type(self):
        self.get_element(one_way_radio).click()
    def test_enter_source_dest_city(self):
        self.get_element(from_city_field).send_keys(source_city)
        self.get_element(dest_city_field).send_keys(dest_city)
    def test_enter_depart_date(self):
        self.get_element(depart_date).send_keys(depart_date_value)
        self.get_element(return_date).send_keys(return_date_value)
        time.sleep(10)