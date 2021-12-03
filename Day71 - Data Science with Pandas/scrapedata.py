# Challenge - read tabular data from website
import requests
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd

endpoint = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
response = requests.get(endpoint).text

soup = BeautifulSoup(response, "html.parser")

inner_btns = soup.find_all("div", {"class": "pagination__btn--inner"})
page_numbers = [inner_btn.getText() for inner_btn in inner_btns if inner_btn.getText().isnumeric()]
total_pages = int(max(page_numbers))

data = []

for page in range(total_pages):
    page_endpoint = f"{endpoint}/page/{page + 1}"
    response = requests.get(page_endpoint)
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("tr", {"class": "data-table__row"})

    for row in rows:
        cells = row.find_all("span", {"class": "data-table__value"})
        record = {
            "Undergraduate Major": cells[1].getText(),
            "Early Career Pay": cells[3].getText().strip("$").replace(",", ""),
            "Mid-Career Pay": cells[4].getText().strip("$").replace(",", ""),
        }
        data.append(record)

df = pd.DataFrame(data).to_csv("salaries_by_college_major_updated.csv", index=False)

