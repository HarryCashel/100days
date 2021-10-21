import requests
import os
import datetime

STOCK = ["TSLA", "IBM"]
COMPANY_NAME = "Tesla Inc"
ALPHA_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"
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


stock_data = get_stock_data()


def get_relevant_info():
    ticker_names = [key for key in stock_data]
    ticker_names = dict.fromkeys(ticker_names)

    for index, key in enumerate(stock_data):
        price = stock_data[key]["05. price"]
        previous_close = stock_data[key]["08. previous close"]
        change_percent = stock_data[key]["10. change percent"]
        ticker_names[key] = {
            "price": price,
            "previous_close": previous_close,
            "change percent": change_percent
        }
    return ticker_names
#
#
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


# def get_recent_articles(info: dict):
#     data = {}
#     for ticker in info:
#


print(get_relevant_info())
print(get_articles(get_relevant_info()))

dic = {"TSLA": None, "IBM": None}

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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
