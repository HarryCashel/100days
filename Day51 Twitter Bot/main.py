from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
USER = "TwitBot56389772"
SERVICE_PROVIDER = "Telstra"


class InternetSpeedTwitter:
    """Class to model expected internet speeds"""

    def __init__(self):
        self.service = Service("C:/Users/cashe/Desktop/chromedriver")
        self.driver = webdriver.Chrome(service=self.service)
        self.down = 260
        self.up = 20
        self.current_down = None
        self.current_up = None

    def get_speed(self):
        """method to get current internet speeds using selenium webdriver to run speedtest via google"""
        self.driver.get("https://www.google.com/")
        self.driver.fullscreen_window()
        search = self.driver.find_element(By.CLASS_NAME, "gLFyf ")
        self.driver.fullscreen_window()
        search.send_keys("speedtest")
        search.send_keys(Keys.RETURN)

        self.driver.find_element(By.ID, "knowledge-verticals-internetspeedtest__test_button").click()

        time.sleep(2)
        try:
            WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "LEARN MORE")))
            self.current_down = self.driver.find_element(By.XPATH,
                                                         '//*[@id="knowledge-verticals-internetspeedtest__download"]/p[1]').text
            self.current_up = self.driver.find_element(By.XPATH,
                                                       '//*[@id="knowledge-verticals-internetspeedtest__upload"]/p[1]').text
        except NoSuchElementException:
            print("Couldn't fetch download or upload speed\n")

    # Old method used before WebDriverWait
    # def wait_for_element(self, classname):
    #     content = self.driver.find_elements(By.CLASS_NAME, classname)
    #     while content[0].text and content[1].text == "" or content[0].text and content[1].text == " ":
    #         content = self.driver.find_elements(By.CLASS_NAME, classname)
    #     return content

    def tweet(self):
        message = f"Hey {SERVICE_PROVIDER}, why is my internet speed {self.current_down}download/{self.current_up}upload when I pay for 175down/25up? "
        if float(self.current_up) < self.up or float(self.current_down) < self.down:
            print("Speeds are slow. Contacting service provider.")
            self.driver.get("https://twitter.com/i/flow/login")
            self.driver.fullscreen_window()

            WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH,
                                                   '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                   '2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))

            email_field = self.driver.find_element(By.XPATH,
                                                   '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                   '2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            email_field.send_keys(EMAIL)
            email_field.send_keys(Keys.RETURN)

            security_check = self.wait_for_field('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                      '2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div['
                                                      '2]/div/input')

            # WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH,
            #                                           '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
            #                                           '2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div['
            #                                           '2]/div/input')))
            #
            # security_check = self.driver.find_element(By.XPATH,
            #                                           '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
            #                                           '2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div['
            #                                           '2]/div/input')
            security_check.send_keys(USER)
            security_check.send_keys(Keys.RETURN)

            password_field = self.wait_for_field('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                      '2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div['
                                                      '2]/div/input')
            # WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH,
            #                                           '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
            #                                           '2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div['
            #                                           '2]/div/input')))
            #
            # password_field = self.driver.find_element(By.XPATH,
            #                                           '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
            #                                           '2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div['
            #                                           '2]/div/input')
            password_field.send_keys(PASSWORD)
            password_field.send_keys(Keys.RETURN)

            search_field = self.wait_for_field('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                    '2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div['
                                                    '1]/div/div/label/div[2]/div/input')

            # search_field = self.driver.find_element(By.XPATH,
            #                                         '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
            #                                         '2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div['
            #                                         '1]/div/div/label/div[2]/div/input')
            search_field.send_keys(SERVICE_PROVIDER)
            search_field.send_keys(Keys.RETURN)
            time.sleep(2)

            first_result = self.wait_for_field('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                    '1]/div/div[2]/div/div/section/div/div/div[3]/div/div/div/div[2]/div['
                                                    '1]/div[1]/a/div/div[1]/div[1]/span/span')

            # first_result = self.driver.find_element(By.XPATH,
            #                                         '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
            #                                         '1]/div/div[2]/div/div/section/div/div/div[3]/div/div/div/div[2]/div['
            #                                         '1]/div[1]/a/div/div[1]/div[1]/span/span')

            if first_result.text == "Telstra":
                first_result.click()

            start_tweet = self.wait_for_field('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div['
                                                   '3]/a/div/span/div/div/span/span')

            # start_tweet = self.driver.find_element(By.XPATH,
            #                                        '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div['
            #                                        '3]/a/div/span/div/div/span/span')
            start_tweet.click()
            # time.sleep(3)
            write_tweet = self.wait_for_field('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                   '2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div['
                                                   '1]/div/div/div/div/div/div/div/div/div/label/div['
                                                   '1]/div/div/div/div/div/div/div/div/div/span[2]/span')

            # write_tweet = self.driver.find_element(By.XPATH,
            #                                        '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
            #                                        '2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div['
            #                                        '1]/div/div/div/div/div/div/div/div/div/label/div['
            #                                        '1]/div/div/div/div/div/div/div/div/div/span[2]/span')
            write_tweet.send_keys(message)

            send_tweet = self.wait_for_field('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                  '2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div['
                                                  '3]/div/div/div[2]/div[4]/div/span/span')
            # send_tweet = self.driver.find_element(By.XPATH,
            #                                       '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
            #                                       '2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div['
            #                                       '3]/div/div/div[2]/div[4]/div/span/span')
            # send_tweet.click()
        else:
            print("Current speeds are good.")

        # try:

        # except:
        #     pass
        # password_field = self.driver.find_element(By.XPATH,
        #                                           '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
        #                                           '2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div['
        #                                           '2]/div/input')
        # password_field.send_keys(PASSWORD)
        # password_field.send_keys(Keys.RETURN)

    def wait_for_field(self, xpath):
        WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH, xpath)))

        field = self.driver.find_element(By.XPATH, xpath)
        return field

    def close(self):
        self.driver.close()


search_speed = InternetSpeedTwitter()
search_speed.get_speed()

print(search_speed.current_down)
print(search_speed.current_up)

search_speed.tweet()
