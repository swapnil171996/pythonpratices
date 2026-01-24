from base.bookingdotcom_base import bookingdotcombase
from .bookingdotcom_locator import *
class bookingdotcomclass(bookingdotcombase):

    def __init__(self,driver):
        super().__init__(driver)
    def open_dummy_website(self,url):
        self.driver.get(url)
    def fight_types(self):
        self.Click_element(one_way)
    def fight_class(self,send_value):
        self.dropdown_select(fight_class,send_value)

    def direct_fight(self):
        self.Click_element(direct_fight)
