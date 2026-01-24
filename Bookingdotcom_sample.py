from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.booking.com/flights/index.html?aid=304142&label=gen173nr-10CAEoggI46AdIM1gEaGyIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4Ar_808oGwAIB0gIkZWNhNTA0N2ItMzFhMy00MzJiLTk5NjQtMzJmZTg3M2IwMGE32AIB4AIB&sid=68d39a0ab13105dddeeaab6c90e91fce&from=booking&")
driver.find_element(By.XPATH,"(//span[contains(@class,'InputRadio-module__field___yOIgZ')])[2]").click()
dropdown=driver.find_element(By.XPATH,"//select[@data-ui-name='cabin_class_input']")
dd_element=Select(dropdown)
dd_element.select_by_value("PREMIUM_ECONOMY")
driver.find_element(By.XPATH,"//input[@data-ui-name='direct_flights_input']").click()
time.sleep(20)
driver.close()
