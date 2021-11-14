from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Users/cashe/Desktop/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")
# content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul
# dates = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
menu = driver.find_element(By.CSS_SELECTOR, ".last .shrubbery .menu")
dates = menu.find_elements(By.TAG_NAME, "time")
texts = menu.find_elements(By.TAG_NAME, "a")

event_dict = {i: {"time": dates[i].text, "name": texts[i].text} for i in range(5)}
print(event_dict)
driver.close()
