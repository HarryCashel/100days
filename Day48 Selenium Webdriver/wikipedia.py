from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Users/cashe/Desktop/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

english_articles = driver.find_element(By.ID, "js-link-box-en")
num_of_articles = english_articles.find_element(By.TAG_NAME, "small bdi")

english_articles.click()

# driver.close()