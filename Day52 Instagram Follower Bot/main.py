from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


# Constants

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
CHROME_DRIVER_PATH = "C:/Users/cashe/Desktop/chromedriver"
INSTA_URL = "https://www.instagram.com/"


class InstagramBot:
    """Class to model an instagram user account and automatically follow accounts"""
    def __init__(self):
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.accounts_to_follow = "fraserwilsonfit"

    def sign_in(self):
        """Method to open and sign into Instagram"""
        self.driver.get("https://www.instagram.com/")
        self.driver.fullscreen_window()

    def search(self):
        search_bar_xpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
        search_bar = self.wait_for_field(xpath=search_bar_xpath)
        search_bar.send_keys(self.accounts_to_follow)
        search_bar.send_keys(Keys.RETURN)


    def get_to_followers(self):
        pass

    def spam_follow(self):
        pass

    def wait_for_field(self, xpath):
        WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH, xpath)))

        field = self.driver.find_element(By.XPATH, xpath)
        return field

instabot = InstagramBot()
instabot.sign_in()
instabot.search()