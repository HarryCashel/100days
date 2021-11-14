from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

# CONSTANTS & SECRETS
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]


# set up service + driver + browser settings
service = Service("C:/Users/cashe/Desktop/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# get LinkedIn job url

driver.get("https://www.linkedin.com/jobs/search/?distance=25&f_AL=true&f_E=1%2C2&f_JT=F%2CI&geoId=104769905&keywords=python%20developer&location=Sydney%2C%20New%20South%20Wales%2C%20Australia&sortBy=R")

time.sleep(2)

# create object for container holding sign in button
# click 'log in' button to go to login page
driver.find_element(By.CSS_SELECTOR, "body > div.base-serp-page > header > nav > div > a.nav__button-secondary").click()

time.sleep(2)

# find and fill out forms then click 'sign in'
email = driver.find_element(By.CSS_SELECTOR, "#username")
email.send_keys(EMAIL)
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button").click()

# Linked has a bot detecting verification step - must sleep and manually complete
