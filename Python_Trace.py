
import pdb;pdb.set_trace() # python debuger

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
wait=WebDriverWait(driver,timeout=20)

def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))

def perform_hover_operation():
    action=ActionChains(driver)
    tester_hub_element = get_element(locator=(By.XPATH, "//div[@id='menu']//a[text()='Tester’s Hub']"))
    action.move_to_element(tester_hub_element)
    action.perform()
    time.sleep(5)

    demo_site_elem=get_element(locator=(By.XPATH,"//span[text()='Demo Testing Site']"))
    action.move_to_element(demo_site_elem)
    action.perform()

    alert_elem=get_element(locator=(By.XPATH,"//span[text()='AlertBox']/parent::a"))
    action.click(alert_elem)
    action.perform()
    time.sleep(5)
    driver.close()
#perform_hover_operation()
def drag_drop():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    iframe_element=get_element(locator=(By.XPATH,"//iframe[@class='demo-frame']"))
    driver.switch_to.frame(iframe_element)
    action=ActionChains(driver)
    image1=get_element(locator=(By.XPATH,"//h5[text()='High Tatras']//parent::li"))
    drag=get_element(locator=(By.XPATH,"//div[@id='trash']"))
    action.drag_and_drop(image1,drag)
    action.perform()

    for i in range(2,5):
        image1 = get_element(locator=(By.XPATH, f"//h5[normalize-space(text())='High Tatras {i}']//parent::li"))
        action.drag_and_drop(image1, drag)
        action.perform()
        time.sleep(5)
        #dropped = get_element(locator=(By.XPATH, f"//div[@id='trash']//h5[normalize-space(text())='High Tatras {i}']/parent::li"))
        #action.drag_and_drop(dropped, get_element(locator=(By.ID, "gallery"))).perform()
        time.sleep(5)
    driver.close()

#drag_drop()

def scroll_to_element():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    Footer_Widget_Area = get_element(locator=(By.XPATH, "//h3[text()='Footer Widget Area 3']"))
    #//li/a[text()='Contact Us']
    action=ActionChains(driver)
    action.scroll_to_element(Footer_Widget_Area)
    #action.scroll_by_amount(100,200)
    action.perform()
    #action.scroll_from_origin()#need to check
    time.sleep(5)
    action.double_click(Footer_Widget_Area)
    driver.close()
#scroll_to_element()
import pyautogui
import pdb;pdb.set_trace()
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


#perform_hover_operation()
