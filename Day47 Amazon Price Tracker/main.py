import requests
from bs4 import BeautifulSoup
import lxml

ITEM_URL = "https://www.amazon.com.au/Optimum-Nutrition-Standard-Pre-Workout-Beta-Alanine/dp/B00PYB335O/ref=sr_1_7" \
           "?keywords=pre+workout&qid=1636690598&sr=8-7 "

browser_headings = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

response = requests.get(url=ITEM_URL, headers=browser_headings)
