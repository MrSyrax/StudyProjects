from bs4 import BeautifulSoup

with open("day45 - web scraping/website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

anchor_tags = soup.find_all(name='a')

print(len(anchor_tags))