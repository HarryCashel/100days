from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
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
SCROLL_PAUSE = .5


class InstagramBot:
    """Class to model an instagram user account and automatically follow accounts"""

    def __init__(self):
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.accounts_to_follow = ["therock", "fraserwilsonfit"]

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

    def search(self, account):
        search_bar_xpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
        search_bar = self.wait_for_field(xpath=search_bar_xpath)
        search_bar.send_keys(account)

        # somewhat verifies first link is accurate to what we are looking for
        WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, account)))
        first_result_link = self.wait_for_field(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        first_result_link.click()

    def get_to_followers(self):
        link_to_followers_xpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        link_to_followers = self.wait_for_field(link_to_followers_xpath)
        link_to_followers.click()

    def spam_follow(self):

        for account in self.accounts_to_follow:
            self.search(account)
            self.get_to_followers()

            followers_list_xpath = '/html/body/div[6]/div/div/div[2]'
            followers_element = self.wait_for_field(followers_list_xpath)

            for i in range(2):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_element)
                time.sleep(3)

            all_buttons = followers_element.find_elements(By.CSS_SELECTOR, 'li button')
            for button in all_buttons:
                try:
                    button.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    cancel_button = self.wait_for_field('/html/body/div[6]/div/div/div[1]/div/div[2]/button')
                    cancel_button.click()

    def wait_for_field(self, xpath):
        WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH, xpath)))

        field = self.driver.find_element(By.XPATH, xpath)
        return field

    def wait_for_button(self, css):
        WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))

        field = self.driver.find_element(By.CSS_SELECTOR, css)
        return field


instabot = InstagramBot()
instabot.sign_in()
instabot.spam_follow()
