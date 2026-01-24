from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class bookingdotcombase:
    def __init__(self,driver,timeout=20):
        self.driver=driver
        self.timeout=timeout
        self.wait=WebDriverWait(driver,timeout)

    def get_element(self,locator):
        element=self.wait.until(ec.presence_of_element_located(locator))
        return element
    def Click_element(self,locator):
        element=self.get_element(locator)
        element.click()
    def Send_keys(self,locator,send_data):
        element=self.get_element(locator)
        element.send_keys(send_data)

    def dropdown_select(self,locator,select_values):
        element=self.get_element(locator)
        dd_element=Select(element)
        dd_element.select_by_value(select_values)



