import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

EMAIL = "cashel.harry101@gmail.com"
PASSWORD = os.environ["PASSWORD"]
MY_PRICE = 50
ITEM_URL = "https://www.amazon.com.au/Optimum-Nutrition-Standard-Pre-Workout-Beta-Alanine/dp/B00PYB335O/ref=sr_1_7" \
           "?keywords=pre+workout&qid=1636690598&sr=8-7 "

browser_headings = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

response = requests.get(url=ITEM_URL, headers=browser_headings).text

soup = BeautifulSoup(response, "lxml")
price = soup.find(name="span", class_="a-offscreen").getText()
title = soup.find(name="span", class_="a-size-large product-title-word-break")

current_price = float(price.split("$")[-1])
format_title = title.getText().strip()

quote = f"{format_title} is currently at {price}.\n{ITEM_URL}"

# if current_price < MY_PRICE:
    # open connection and send email
with smtplib.SMTP("smtp.gmail.com") as connection:
    # open connection with tls
    connection.starttls()

    # log into email provider
    connection.login(user=EMAIL, password=PASSWORD)

    # send mail
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg=f"Subject:Amazon Price Alert\n\n{quote}"
    )
