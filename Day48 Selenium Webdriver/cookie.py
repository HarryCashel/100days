import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:/Users/cashe/Desktop/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# get the url
driver.get("https://orteil.dashnet.org/cookieclicker/")

# create objects of needed elements
cookie = driver.find_element(By.ID, "bigCookie")
time.sleep(5)

popup = driver.find_element(By.CLASS_NAME, "cc_banner")
click = popup.find_element(By.TAG_NAME, "a")
click.click()


def buy_upgrades():
    pass


def buy_product(money, dictionary):
    can_afford = {price: id_ for price, id_ in dictionary.items() if price < money}

    best = max(can_afford)
    print(best)
    purchase_id = dictionary[best]
    for i in range(10):
        driver.find_element(By.ID, purchase_id).click()


def create_product_dictionary():
    product_element = driver.find_element(By.ID, "products")
    products = product_element.find_elements(By.CLASS_NAME, "product")
    product_prices = product_element.find_elements(By.CLASS_NAME, "price")
    prices = [int(price.text.replace(",", "")) for price in product_prices if price.text != ""]
    ids = [product.get_attribute("id") for product in products]

    result = {prices[i]: ids[i] for i in range(len(prices))}
    return result


def upgrade():
    upgrades_element = driver.find_element(By.ID, "upgrades")
    upgrades = upgrades_element.find_elements(By.TAG_NAME, "div")
    for u in upgrades:
        u.click()


now = time.time()
five_min = now + 300
timeout = time.time() + 5
while time.time() < five_min:

    cookie.click()
    if time.time() > timeout:
        bank = driver.find_element(By.ID, "cookies").text.split()[0].replace(",", "")

        bank = int(bank)
        upgrade()
        product_dic = create_product_dictionary()
        buy_product(bank, product_dic)
        # enabled_products[-1].click()
        timeout = time.time() + 5
