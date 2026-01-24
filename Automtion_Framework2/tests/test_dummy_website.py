import time

from selenium import webdriver

import pytest

from module.dummy_website_class import dummy_website

@pytest.mark.usefixtures("get_driver")
class Test_dummy_website:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dp=dummy_website(self.driver)

    def test_open_dummy_website(self):
        self.dp.open_dummy_website("https://sqatools.in/dummy-booking-website/")
        self.dp.choose_correct_option()
        self.dp.enter_value_first_name("Kishor")
        self.dp.enter_value_last_name("patil")
        self.dp.enter_value_dob("12/03/1993")
        self.dp.select_gender()
        self.dp.select_number_of_passangers("2")


    def test_Travel_details(self):
        self.dp.Travel_details()
        self.dp.Source_city_name("Pune")
        self.dp.destination_city_name("Mumbai")
        self.dp.Departure_date("12/05/2025")
        self.dp.Return_date("11/09/2026")

    def test_delivery_options(self):
        self.dp.Delivery_Options("10/09/2025")
        self.dp.receive_the_dummy_ticket()

    def test_Billing_details(self):
        self.dp.Billing_name("Swapnil Patil")
        self.dp.Pnone_num("9989908990")
        self.dp.Email_address("patils@gmail.com")
        self.dp.Street_address("somnath nagar")
        self.dp.Stress_address1("ramtekdi")
        self.dp.Postcode("411014")
        self.dp.select_country_dd("DZ")

    def test_Most_Visited_Cities(self):
        self.dp.Most_Visited_Cities()





        """
    def test_Travel_details(self):
        self.dp.Travel_details.Click_element()
        self.dp.Travel_details.Send_text("Pune")
        self.dp.Travel_details.Send_text("Mumbai")
        self.dp.Travel_details.Send_text("12/12/2025")
        self.dp.Travel_details.Send_text("12/12/2025")


error:-
 def test_Travel_details(self):
        #self.dp.Click_element(oneway)
>       self.dp.Send_text("Pune")
E       TypeError: selenium_base.Send_text() missing 1 required positional argument: 'send_value'
"""






