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

# print(rental_links)
