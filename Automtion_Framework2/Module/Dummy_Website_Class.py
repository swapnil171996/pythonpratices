from selenium.webdriver.common.by import By

from base.dummy_selenium_base import selenium_base
from .dummy_website_locator import  *
class dummy_website(selenium_base):
    def __init__(self,driver):
        super().__init__(driver)
    def open_dummy_website(self,url):
        self.driver.get(url)
    def choose_correct_option(self):
        self.Click_element(Dummy_return_ticket)
    def enter_value_first_name(self,send_data):
        self.Send_text(first_name,send_data)
    def enter_value_last_name(self,send_datas):
        self.Send_text(last_name,send_datas)
    def enter_value_dob(self,dob_data):
        self.Send_text(DOB,dob_data)
    def select_gender(self):
        self.Click_element(gender)
    def select_number_of_passangers(self,select_values):
        self.Select_from_Dropdown(Addition_of_member,select_values)

    def Travel_details(self):
        self.Click_element(oneway)

    def Source_city_name(self, source_city):
        self.Send_text(From_City, source_city)

    def destination_city_name(self,dest_city):
        self.Send_text(Destination_City,dest_city)
    def Departure_date(self,dept_date):
        self.Send_text(Departure_date, dept_date)
    def Return_date(self,return_date):
        self.Send_text(Return_date, return_date)
    def Delivery_Options(self,appo_date):
        self.Send_text(Appointment_Date,appo_date)
    def receive_the_dummy_ticket(self):
        self.Click_element(Receive_Optional)
    def Billing_name(self,bill_name):
        self.Send_text(Billing_Name,bill_name)
    def Pnone_num(self,phone_num):
        self.Send_text(Phone,phone_num)
    def Email_address(self,email):
        self.Send_text(Email_address, email)
    def Street_address(self,street):
        self.Send_text(Street_adress, street)
    def Stress_address1(self,stree1):
        self.Send_text(Stress_address1, stree1)
    def Postcode(self,post_code):
        self.Send_text(Postcode, post_code)
    def select_country_dd(self,select_country):
        self.Select_from_Dropdown(Country, select_country)

    def Most_Visited_Cities(self):
        self.Click_element(checkbox)


'''
    def Travel_details(self,source_city,dest_city,dept_date,return_date):
        self.Click_element(oneway)
        self.Send_text(From_City,source_city)
        self.Send_text(Destination_City, dest_city)
        self.Send_text(Departure_date, dept_date)
        self.Send_text(Return_date, return_date)
'''

'''
    def Delivery_Options(self,appo_date):
        self.Send_text(Appointment_Date,appo_date)
        self.Click_element(Receive_Optional)

    def Billing_details(self,bill_name,phone_num,email,street,select_country,post_code,street1):
        self.Send_text(Billing_Name, bill_name)
        self.Send_text(Phone,phone_num)
        self.Send_text(Email_address,email)
        self.Send_text(Street_adress,street)
        self.Send_text(Stress_address1,stree1)
        self.Send_text(Postcode,post_code)
        self.Select_from_Dropdown(Country,select_country)

    def Most_Visited_Cities(self):
        self.Click_element(checkbox)
'''











