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
t1=time.time()
driver.get("https://sqatools.in/dummy-booking-website/")
try:
    driver.find_element(By.CSS_SELECTOR,'input[name="fromcyuity"]').send_keys("Mumbai")

except:
    pass

t2=time.time()
print("total time :",t2-t1) #total time : 10.951991081237793
time.sleep(10)
driver.close()