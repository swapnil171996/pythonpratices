import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://sqatools.in/dummy-booking-website/")
driver.implicitly_wait(10)
wait=WebDriverWait(driver,timeout=20)

def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))

get_element(locator=(By.CSS_SELECTOR,"#billing_email")).send_keys("Swapnil.patil@gmail.com")
get_element(locator=(By.CSS_SELECTOR,"#billing_address")).send_keys("Sainathnagar,Kharadi")
dropdown=get_element(locator=(By.CSS_SELECTOR,"#billing_country"))
drop_element=Select(dropdown)
#drop_element.select_by_index(4)#Andorra
drop_element.select_by_value("DZ")#Algeria
#drop_element.select_by_visible_text("India")#India
print(drop_element.first_selected_option.text)
time.sleep(10)
driver.close()

