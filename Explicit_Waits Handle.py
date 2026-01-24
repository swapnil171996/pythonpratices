'''
implicit wait
explicit wait
flauent wait
static wait

'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
Wait=WebDriverWait(driver,timeout=20)
#WebDriverWait(driver,timeout=20,poll_frequency=2)
#default poll_frequency is 0.5 sec
t1=time.time()
driver.get("https://sqatools.in/dummy-booking-website/")
try:
    driver.find_element(By.CSS_SELECTOR,'input[name="fromcity"]').send_keys("Mumbai")
    driver.find_element(By.CSS_SELECTOR,'input[name*="dest"]').send_keys("Pune")
except:
    pass
t2=time.time()
print("Total Time",t2-t1)#Total Time 0.9566271305084229 with correct locator
#Total Time 10.883427619934082 with wrong locator
a1=time.time()
try:
    Wait.until(ec.visibility_of_element_located((By.ID,'billaing_name'))).send_keys("Pune")
except:
    pass
a2=time.time()
print("Total time ofbilling name",a2-a1) #Total time ofbilling name 0.10413479804992676 with correct locator
#Total time ofbilling name 21.10432481765747 with wrong locator
time.sleep(10)
driver.close()

'''
1. Presence of Element
Waits until the element exists in the DOM (not necessarily visible).
element = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.ID, "billing_name"))
)

2.2. Visibility of Element
Waits until the element is visible on the page.
element = WebDriverWait(driver, 10).until(
    ec.visibility_of_element_located((By.XPATH, '//input[@name="fromcity"]'))
)

3. Element to be Clickable
Waits until the element is visible and enabled.
button = WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.CSS_SELECTOR, 'button#submit'))
)
button.click()

4.Text to be Present in Element
Waits until specific text appears inside an element
WebDriverWait(driver, 10).until(
    ec.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Dummy Ticket Booking Website")
)
5.. Alert is Present
Waits until a JavaScript alert pops up
alert = WebDriverWait(driver, 10).until(ec.alert_is_present())
print(alert.text)
alert.accept()
6.Frame Available and Switch
Waits until a frame is available, then switches to it.
WebDriverWait(driver, 10).until(
    ec.frame_to_be_available_and_switch_to_it((By.NAME, "frameName"))
)

7. Invisibility of Element
Waits until an element disappears.
WebDriverWait(driver, 10).until(
    ec.invisibility_of_element_located((By.ID, "loading_spinner"))
)



'''