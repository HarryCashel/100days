from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

# CONSTANTS & SECRETS
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]


def run_through_application():
    submit_button = driver.find_elements(By.CSS_SELECTOR, "footer button")[-1]

    submit_button.click()
    time.sleep(1.5)
    submit_button = driver.find_elements(By.CSS_SELECTOR, "footer button")[-1]
    submit_button.click()
    time.sleep(1.5)

    try:
        forms = driver.find_elements(By.CLASS_NAME, "jobs-easy-apply-form-section__grouping")
        for form in forms:
            input_form = form.find_element(By.CSS_SELECTOR, "input")
            if input_form.get_attribute("type") == "text":
                input_form.send_keys("2")
            elif input_form.get_attribute("type") == "radio":
                text = form.find_element(By.CLASS_NAME, "t-14").text
                if "legally" in text:
                    print(input_form.get_attribute("checked"))
                    print(input_form.is_selected())
                elif "sponsorship" in text:
                    print(input_form.get_attribute("checked"))
                    print(input_form.is_selected())
                elif "commuting" in text:
                    print(input_form.get_attribute("checked"))
                    print(input_form.is_selected())

        submit_button = driver.find_elements(By.CSS_SELECTOR, "footer button")[-1]
        submit_button.click()
        time.sleep(1.5)
    except:
        pass

    try:
        submit_button = driver.find_elements(By.CSS_SELECTOR, "footer button")[-1]
        submit_button.click()
        time.sleep(2)

        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()
        time.sleep(2)
        discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
        discard_button.click()
        print("Complex application, skipped.")
    except:
        pass


# urn\:li\:fs_easyApplyFormElement\:\(urn\:li\:fs_normalized_jobPosting\:2764618936\,35800637\,numeric\)
# ember431 > div > form > div > div > div:nth-child(2) > div > div > div
# set up service + driver + browser settings
service = Service("C:/Users/cashe/Desktop/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# get LinkedIn job url

driver.get(
    "https://www.linkedin.com/jobs/search/?distance=25&f_AL=true&f_E=1%2C2&f_JT=F%2CI&geoId=104769905&keywords=python%20developer&location=Sydney%2C%20New%20South%20Wales%2C%20Australia&sortBy=R")

time.sleep(2)

# create object for container holding sign in button
# click 'log in' button to go to login page
driver.find_element(By.CSS_SELECTOR, "body > div.base-serp-page > header > nav > div > a.nav__button-secondary").click()

time.sleep(2)

# find and fill out forms then click 'sign in'
email = driver.find_element(By.CSS_SELECTOR, "#username")
email.send_keys(EMAIL)
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button").click()

# Linked has a bot detecting verification step - must sleep and manually complete
# seemingly happens occasionally
time.sleep(2)

# check for messaging pop up and close if reachable

try:
    driver.find_element(By.CSS_SELECTOR, "#ember202 > li-icon > svg").click()
except NoSuchElementException:
    pass

# create list of jobs
job_element = driver.find_element(By.CSS_SELECTOR,
                                  "body > div.application-outlet > div.authentication-outlet > div.job-search-ext > div.jobs-search-two-pane__wrapper > div > section.jobs-search__left-rail > div > div > ul")
list_of_jobs = job_element.find_elements(By.TAG_NAME, "li")

for i in range(len(list_of_jobs)):
    list_of_jobs = job_element.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
    list_of_jobs[i].click()
    print("click")
    time.sleep(4)
    apply_div = driver.find_element(By.CSS_SELECTOR,
                                    "body > div.application-outlet > div.authentication-outlet > div.job-search-ext > div.jobs-search-two-pane__wrapper > div > section.jobs-search__right-rail > div > div > div:nth-child(1) > div > div:nth-child(1) > div > div.jobs-unified-top-card__content--two-pane > div:nth-child(4) > div > div > div")
    apply_div.click()
    time.sleep(2)

    run_through_application()
    time.sleep(2)
