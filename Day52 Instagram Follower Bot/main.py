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
        self.accounts_to_follow = "therock"

    def sign_in(self):
        """Method to open and sign into Instagram"""
        self.driver.get("https://www.instagram.com/")
        self.driver.fullscreen_window()

        email_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        email_field = self.wait_for_field(email_xpath)
        email_field.send_keys(EMAIL)

        password_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        password_field = self.wait_for_field(password_xpath)
        password_field.send_keys(PASSWORD)

        password_field.send_keys(Keys.RETURN)

    def search(self):
        search_bar_xpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
        search_bar = self.wait_for_field(xpath=search_bar_xpath)
        search_bar.send_keys(self.accounts_to_follow)

        # somewhat verifies first link is accurate to what we are looking for
        WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, self.accounts_to_follow)))
        first_result_link = self.wait_for_field(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        first_result_link.click()

    def get_to_followers(self):
        link_to_followers_xpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        link_to_followers = self.wait_for_field(link_to_followers_xpath)
        link_to_followers.click()

    def spam_follow(self):
        pass

    def wait_for_field(self, xpath):
        WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH, xpath)))

        field = self.driver.find_element(By.XPATH, xpath)
        return field


instabot = InstagramBot()
instabot.sign_in()
instabot.search()
instabot.get_to_followers()
