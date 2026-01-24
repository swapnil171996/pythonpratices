from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class selenium_base:
    def __init__(self,driver,timeout=20):
        self.driver=driver
        self.timeout=timeout
        self.wait=WebDriverWait(self.driver,self.timeout)
        self.log=logging.getLogger(__name__)

    def get_element(self,locator):
        try:
            element=self.wait.until(ec.presence_of_element_located(locator))
            return element
        except Exception as e:
            self.log.info(f"element not found :{locator}")
            self.log.info(e)
            element.screenshot("logs/element_not_found.png")


    def Click_element(self,locator):
        self.log.info(f"finding element with {locator}")
        element=self.get_element(locator)
        element.click()

    def Select_from_Dropdown(self,locator,select_value):
        self.log.info(f"select:{select_value} value from dropown :{locator}")
        dd=self.get_element(locator)
        dd_element=Select(dd)
        dd_element.select_by_value(select_value)
    def Send_text(self,locator,send_value):
        self.log.info(f"sending text:{send_value} to element:{locator}")
        element=self.get_element(locator)
        element.clear()
        element.send_keys(send_value)
    def radio_button(self,locator):
        element=self.get_element(locator)
        return {
            "enabled": element.is_enabled(),
            "selected": element.is_selected()
        }






