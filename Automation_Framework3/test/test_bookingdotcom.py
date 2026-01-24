import pytest

from module.bookingdotcom_class import bookingdotcomclass
@pytest.mark.usefixtures("get_driver")
class Test_bookingdocom:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.bk=bookingdotcomclass(self.driver)

    def test_fight_type(self):
        self.bk.open_dummy_website("https://www.booking.com/flights/index.html?aid=304142&label=gen173nr-10CAEoggI46AdIM1gEaGyIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4Ar_808oGwAIB0gIkZWNhNTA0N2ItMzFhMy00MzJiLTk5NjQtMzJmZTg3M2IwMGE32AIB4AIB&sid=68d39a0ab13105dddeeaab6c90e91fce&from=booking&")
        self.bk.fight_types()
        #self.bk.fight_class("PREMIUM_ECONOMY")
        self.bk.direct_fight()





