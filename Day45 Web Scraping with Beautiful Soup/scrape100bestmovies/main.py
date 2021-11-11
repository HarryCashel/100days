import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

all_titles = soup.find_all(name="h3")

list_in_order = [title.getText() for title in all_titles]

with open("moves.txt", mode="a") as file:
    for item in reversed(list_in_order):
        file.write(f"{item}\n")