
#Alerts
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,timeout=20)
driver.get("https://sqatools.in/python-tutorials/")
def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))
def handler_alert_box():
    get_element(locator=(By.ID,"btnshowing")).click()
    alert1=Alert(driver)
    print(alert1.text)
    time.sleep(5)
    alert1.accept()

handler_alert_box()
time.sleep(5)
driver.close()

def handler_confim_box():
    get_element(locator=(By. ID,"button")).click()
    alert2=Alert(driver)
    print(alert2.text)
    time.sleep(5)
    alert2.accept()
    para_ele_ok=get_element(locator=(By. ID,"demo"))
    print(para_ele_ok.text)
    assert para_ele_ok.text=="You pressed ok!"

    get_element(locator=(By.ID,"button")).click()
    time.sleep(5)
    alert2.dismiss()
    para_ele_dismiss=get_element(locator=(By.ID,"demo"))
    print(para_ele_dismiss.text)
    assert para_ele_dismiss.text=="You pressed cancel!"


handler_confim_box()
    def handler_prompt_box(name):
        get_element(locator=(By.ID,"promptbtn")).click()
        alert3=Alert(driver)
        print(alert3.text)
        alert3.send_keys(name)
        time.sleep(5)
        alert3.accept()
        prompt_msg=get_element(locator=(By.ID,"prompt"))
        print(prompt_msg.text)
        assert prompt_msg.text==(f"Hello {name}!How "
                                 f" you")


handler_prompt_box("gtm"):
time.sleep(5)
driver.close()
