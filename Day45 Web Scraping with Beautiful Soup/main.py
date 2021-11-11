from bs4 import BeautifulSoup

# open the html file
with open("website.html", encoding="utf-8") as file:
    content = file.read()

# create soup object of html file
soup = BeautifulSoup(content, "html.parser")

# find first title tag and title content
print(soup.title)
print(soup.title.name)
print(soup.title.string)

# print(soup.prettify())
# find first anchor tag
print(soup.a)

# create list of all anchor tags

all_anchor_tags = soup.find_all(name="a")

print(all_anchor_tags)

# loop through and print the text of each anchor tag
for tag in all_anchor_tags:
    print(tag.getText())

# loop through and get the links of each anchor tag
for tag in all_anchor_tags:
    print(tag.get("href"))

# find an element by tag and id
heading = soup.find(name="h1", id="name")
print(heading)

# find an element by tag and class name
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# find an anchor tag that sits inside a paragraph tag
company_url = soup.select_one(selector="p a")
print(company_url)

# find an anchor tag using it's id
name = soup.select_one(selector="#name")

# find an element using class
headings = soup.select(".heading")
