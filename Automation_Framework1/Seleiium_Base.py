from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
class SeleniumBase:
    def __init__(self,driver,timeout=30):
        self.driver=driver
        self.timeout=timeout
        self.wait=WebDriverWait(self.driver,self.timeout)
    def get_element(self,locator):
        element=self.wait.until(ec.presence_of_element_located(locator))
        return element
    def click_element(self,locator):
        element=self.get_element(locator)
        element.click()
    def send_text(self,locator,data):
        element=self.get_element(locator)
        element.clear()
        element.send_keys(data)
    def select_value_from_dropdown(self,locator,text_value):
        element=self.get_element(locator)
        select=Select(element)
        select.select_by_visible_text(text_value)




