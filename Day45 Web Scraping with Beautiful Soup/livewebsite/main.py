import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

all_story_links = soup.find_all(name="a", class_="titlelink")

# for link in all_story_links:
#     print(link.get("href"))

article_links = [link.get("href") for link in all_story_links]
article_texts = [link.getText() for link in all_story_links]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

highest = 0
for num in article_upvotes:
    if num > highest:
        highest = num
index = article_upvotes.index(highest)
print(article_texts[index], article_links[index], article_upvotes[index])