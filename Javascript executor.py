import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/dummy-booking-website/")
website_title=driver.execute_script("return document.title;")
print(website_title) #Dummy Booking Website - SQA Tools

from_city_element=driver.execute_script("return document.getElementById('fromcity');")
from_city_element.send_keys("Mumbai")

dest_city_element=driver.execute_script("return document.getElementById('destcity');")
dest_city_element.send_keys("Bangalore")
time.sleep(10)

''''''''''''''''''''''''''
#upload file

driver.get("https://sqatools.in/dummy-booking-website/")
#to upload file add file path in send keys
driver.find_element(By.ID,"myfile").send_keys("E://Fileshare\\count_name.text")
#click on submit button
driver.find_element((By.XPATH,"//input[@id='myFile//following-sibling::input[@type=submit']"))

