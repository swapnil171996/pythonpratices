import time

from selenium.webdriver.common.by import  By
first_name=(By.XPATH,'(//input[@name="firstname"])[1]')
last_name=((By.XPATH,'(//input[@name="firstname"])[2]'))
Dummy_return_ticket=(By.XPATH,"//input[@value='radio_345']")
DOB=(By.XPATH,"//input[@id='birthday']")
gender=(By.XPATH,"//input[@id='male']")
Addition_of_member=(By.XPATH,"//select[@id='admorepass']")
oneway=(By.XPATH,"//input[@id='oneway']")
From_City=(By.XPATH,"//input[@id='fromcity']")
Destination_City=(By.XPATH,"//input[@name='destcity']")
Departure_date=(By.XPATH,"//input[@name='departdate']")
Return_date=(By.XPATH,"//input[@name='returndate']")
Appointment_Date=(By.XPATH,"//input[@name='visadate']")
Receive_Optional=(By.XPATH,"(//input[@id='female'])[2]")
Billing_Name=(By.XPATH,"//input[@id='billing_name']")
Phone=(By.XPATH,"//input[@id='billing_phone']")
Email_address=(By.XPATH,"//input[@id='billing_email']")
Street_adress=(By.XPATH,"//input[@id='billing_address']")
Country=(By.XPATH,"//select[@id='billing_country']")
Postcode=(By.XPATH,"//input[@name='postcode']")
Stress_address1=(By.XPATH,"//input[@id='street_address1']")
checkbox=(By.XPATH,"//td[text()='6001']/preceding-sibling::td//input")









