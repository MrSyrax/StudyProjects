from bs4 import BeautifulSoup

with open("day45 - web scraping/website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title)
print(soup.title.name)