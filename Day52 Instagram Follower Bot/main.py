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


# class InstagramBot:
#     """Class to model an instagram user account and automatically follow accounts"""
#     def __init__(self):
#         self.service = Service(CHROME_DRIVER_PATH)