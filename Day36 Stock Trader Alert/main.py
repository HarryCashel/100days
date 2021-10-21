"""REVIEW - MAKE EACH API SECTION A CLASS IN SEPARATE MODULES"""

import requests
import os
import datetime
from twilio.rest import Client

# Constants and env variables
STOCK = ["TSLA", "GOOG", "AAPL"]
ALPHA_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"

TWILIO_PH_NUM = "+18575778643"
TWILIO_SID = os.environ["TWILIO_ACC_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
MY_NUM = os.environ["MY_NUM"]

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)


def get_stock_data():
    data = {}

    for ticker in STOCK:
        response = requests.get(url=ALPHA_URL,
                                params={
                                    "function": "GLOBAL_QUOTE",
                                    "symbol": ticker,
                                    "apikey": os.environ["ALPHA_KEY"]
                                })
        data[ticker] = response.json()["Global Quote"]

    return data


def get_relevant_info(info: dict):
    ticker_names = [key for key in info]
    ticker_names = dict.fromkeys(ticker_names)

    for index, key in enumerate(info):
        price = info[key]["05. price"]
        previous_close = info[key]["08. previous close"]
        change_percent = info[key]["10. change percent"]
        ticker_names[key] = {
            "price": price,
            "previous_close": previous_close,
            "change percent": change_percent
        }
    return ticker_names


def get_articles(info: dict):
    data = {}
    for ticker in info:
        response = requests.get(NEWS_URL, params={
            "apiKey": os.environ["NEWS_API_KEY"],
            "q": ticker,
            "from_param": yesterday,
            "to": today
        })
        data[ticker] = response.json()
    return data


def get_recent_articles(info: dict) -> dict:
    data = {}
    for ticker in info:
        most_recent_title = [i["title"] for i in info[ticker]["articles"][:3]]
        most_recent_description = [i["description"] for i in info[ticker]["articles"][:3]]
        data[ticker] = {most_recent_title[i]: most_recent_description[i] for i in range(len(most_recent_title))}
    return data


stock_data = (get_relevant_info(get_stock_data()))
relevant_stock_news = get_recent_articles(get_articles(stock_data))


def format_news():
    data = []

    for item in stock_data:
        change = float(stock_data[item]["change percent"].replace("%", ""))
        if abs(change) > .1:

            for news in relevant_stock_news[item]:
                if change > .1:
                    icon = "🔺"
                elif change < .1:
                    icon = "🔻"
                data.append(
                    f"\n{item}: {icon}{change}% "
                    f"\nHeadline: {news} "
                    f"\nBrief: {relevant_stock_news[item][news]} "
                )
    return data


def send_message(data: list):
    for i in range(len(data)):
        message = data[i]
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
                body=message,
                from_=TWILIO_PH_NUM,
                to=MY_NUM
            )
    print(message.status)


send_message(format_news())

# for i in range(len(format_news())):
#     print(format_news()[i])
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
