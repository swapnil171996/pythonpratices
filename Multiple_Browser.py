import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
browser="chrome"
driver=None
if browser=="chrome":
    driver=webdriver.Chrome()
elif browser=="edge":
    #driver = webdriver.Edge(executable_path="C:\\Driver\\msedgedriver.exe")
    service = Service(r"C:\\Driver\\msedgedriver.exe")
    driver = webdriver.Edge(service=service)


elif browser=="Firefox":
    driver=webdriver.Firefox()

driver.maximize_window()
driver.get("https://sqatools.in/dummy-booking-website/")
driver.implicitly_wait(10)
wait=WebDriverWait(driver,timeout=20)
def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))
get_element(locator=(By.CSS_SELECTOR,'input[name="fromcity"]')).send_keys("Mumbai")
get_element(locator=(By.CSS_SELECTOR,'input[name*="dest"]')).send_keys("pune")
time.sleep(10)
driver.close()
wait.until(ec.)