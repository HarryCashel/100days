from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Users/cashe/Desktop/chromedriver")
driver = webdriver.Chrome(service=service)

# Get the url
driver.get("https://www.wikipedia.org/")

# Create selenium objects of our desired elements
english_articles = driver.find_element(By.ID, "js-link-box-en")
num_of_articles = english_articles.find_element(By.TAG_NAME, "small bdi")

# Click link
english_articles.click()

# Locate search bar
search_bar = driver.find_element(By.ID, "searchInput")
search_bar.send_keys("Python")
search_bar.submit()
# driver.close()