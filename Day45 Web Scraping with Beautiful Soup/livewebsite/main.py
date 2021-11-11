import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

all_story_links = soup.find_all(name="a", class_="titlelink")
scores = soup.find_all(name="span", class_="score")


# for link in all_story_links:
#     print(link.get("href"))

for link in all_story_links:
    print(link.getText())
for score in scores:
    print(score.getText())
