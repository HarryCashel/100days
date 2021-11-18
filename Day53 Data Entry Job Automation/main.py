import time
import os
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSc-0shJnO4A6gmSDOAKuAL3RAH8DG3xX-ikVuTjqswX9OD3rg" \
                   "/viewform?usp=sf_link "
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
             "%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A" \
             "-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C" \
             "%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A" \
             "%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse" \
             "%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B" \
             "%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D" \
             "%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min" \
             "%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D "
CHROME_DRIVER_PATH = "C:/Users/cashe/Desktop/chromedriver"


class DataEntry:
    def __init__(self):
        self.header = browser_headings = {
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/95.0.4638.69 Safari/537.36 "
        }
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)

    # method for scraping
    def get_listings(self):
        response = requests.get(url=ZILLOW_URL, headers=self.header).text
        soup = BeautifulSoup(response, "html.parser")

        rental_links = soup.select(".list-card-info")
        rental_links.remove(rental_links[-1])

        house_data = [{
            "price": link.findChild(class_="list-card-price").text.replace("/$+", ""),
            "address": link.findChild(class_="list-card-addr").text,
            "link": link.findChild(class_="list-card-link")["href"]
        } for link in rental_links]

        return house_data

    def fill_form(self, listing):
        url = GOOGLE_FORM_LINK
        self.driver.get(url)
        for listing in listing:
            address_form = self.wait_for_field('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                               '1]/div/div[1]/input')
            price_form = self.wait_for_field('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                             '1]/div/div[1]/input')
            link_form = self.wait_for_field('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                            '1]/div/div[1]/input')

            address_form.send_keys(listing["address"])
            price_form.send_keys(listing["price"])
            link_form.send_keys(listing["link"])
            self.reset_form()
        print("All listing uploaded to Google Form")
        print("Exiting program.")
        self.driver.close()

    def reset_form(self):
        submit = self.wait_for_field('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        submit.click()
        reset = self.wait_for_field('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        reset.click()

    def wait_for_field(self, xpath):
        WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH, xpath)))

        field = self.driver.find_element(By.XPATH, xpath)
        return field

    def scroll_down(self):
        self.driver.get(ZILLOW_URL)
        self.driver.fullscreen_window()
        listings_card = self.wait_for_field('//*[@id="grid-search-results"]')
        for i in range(2):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", listings_card)
            time.sleep(1)

test = DataEntry()
listings = test.get_listings()
test.fill_form(listings)
# test.scroll_down()