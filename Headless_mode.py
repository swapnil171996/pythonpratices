from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
#headless mode:Running a browser without opening its GUI
#its uses when we test in diffrent environment ex.linux
chro_option=Options()
chro_option.add_argument('--headless')
driver=webdriver.Chrome(options=chro_option)
import pyautogui
import time
wait=WebDriverWait(driver,timeout=20)

def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))
def Context_click_element():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    time.sleep(10)
    Context_element=get_element(locator=(By.XPATH,"//a[text()='About']"))
    action=ActionChains(driver)
    action.context_click(Context_element)
    action.perform()
    pyautogui.press('down')
    pyautogui.press('down')
    time.sleep(3)
    pyautogui.press('enter')

    time.sleep(20)

Context_click_element()