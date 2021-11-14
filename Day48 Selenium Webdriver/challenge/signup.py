from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Users/cashe/Desktop/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Harry")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Cashel")

email = driver.find_element(By.NAME, "email")
email.send_keys("c.h@gmail.com")

email.submit()