import time

from google_pageclass import GooglePage
import pytest


@pytest.mark.usefixtures("get_driver")
class TestGooglesearch:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gp=GooglePage(self.driver)
    def test_search_on_google(self):
        self.gp.open_google_page("https://www.google.com/")
        self.gp.enter_value_to_search_box("Python Selenium")
        self.gp.clik_to_search_button()
        time.sleep(10)