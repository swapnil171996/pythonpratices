import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/python-tutorials/")
wait=WebDriverWait(driver,timeout=20)
def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))

element=get_element(locator=(By.LINK_TEXT,"Python Variables"))
element.click()
browser_hand=driver.window_handles
print("browser wndows",browser_hand)
#switching to new browser tab
driver.switch_to.window(browser_hand[1])
element1=get_element(locator=(By.XPATH,'//h2[normalize-space()="Python Variable Types:"]'))
assert element1
print(element1.text)
time.sleep(5)
driver.close()

#switching back to main window
driver.switch_to.window(browser_hand[0])
get_element(locator=(By.XPATH,'//li/a[normalize-space()="Home"]')).click()

'''
till function is same code as above

link_text=['smoke testing','Monkey Testing','Ad-hoc Testing']

for text_value in links_text:
    get_element(locator=(By.LINK_TEXT,text_value"]')).click()
    
windows_list=driver.window_handles
for window_id in windows_list[1:]:
    driver.switch_to.window(window_id)
    print(driver.current_url)
    time.sleep(3)
    driver.close()
    
driver.switch_to.window(window_list[0)
get_element(locator=(By.LINK_TEXT,Home"]')).click()
 time.sleep(3)
driver.close()
    




'''
