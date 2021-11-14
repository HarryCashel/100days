from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:/Users/cashe/Desktop/chromedriver")
driver = webdriver.Chrome(service=service)

# get the url
driver.get("https://orteil.dashnet.org/cookieclicker/")

# create objects of needed elements
cookie = driver.find_element(By.ID, "bigCookie")
upgrades_element = driver.find_element(By.ID, "upgrades")
store = driver.find_element(By.ID, "products")

enabled_upgrades = upgrades_element.find_elements(By.CLASS_NAME, "crate upgrades enabled")
