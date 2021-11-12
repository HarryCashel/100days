from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Users/cashe/Desktop/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get(
    "https://www.amazon.com.au/Optimum-Nutrition-Standard-Pre-Workout-Beta-Alanine/dp/B00PYB335O/ref=sr_1_7"
    "?keywords=pre+workout&qid=1636690598&sr=8-7 "
)

price = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[1]')
# price = driver.find_element(By.CSS_SELECTOR, "span.a-offscreen+span")
print(price.get_attribute("innerText"))

driver.close()
