import smtplib
from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
empire_web_page = response.text
soup = BeautifulSoup(empire_web_page, 'html.parser')
print(empire_web_page)

top_100 = soup.find_all(name='h3',class_='title')
top_100_reversed = top_100[::-1]
titles = [h3.getText() for h3 in top_100_reversed]

try:
    with open('day45 - web scraping/top_100.txt', 'a') as file:
        for h3 in titles:
            file.write(f'{h3}\n')
except FileNotFoundError:
    with open('day45 - web scraping/top_100.txt', 'w') as file:
         for h3 in titles:
            file.write(f'{h3}\n')


#------------------------------FIRST WEBSITE SCRAPED----------------#

# url = 'https://news.ycombinator.com/'

# response = requests.get(url)
# yc_web_page = response.text

# soup = BeautifulSoup(yc_web_page, 'html.parser')

# titlelink = soup.find_all(name='a', class_='titlelink')
# article_text = []
# article_link = []


# for line in titlelink:
#     article_text.append(line.getText())
#     article_link.append(line.get('href'))


# article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]


# print(article_text)
# print(article_link)
# print(article_upvote)

# max_upvote = max(article_upvote)
# max_upvote_index = article_upvote.index(max_upvote)
# top_article = article_text[max_upvote_index]
# top_article_link = article_link[max_upvote_index]


# print(top_article)
# print(top_article_link)
# print(max_upvote)

#---------------------------------------What is available to use from beautiful soup-------------------#

# with open('day45 - web scraping/website.html', encoding='utf8') as file:
#     contents = file.read()


# soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title)

# print(soup.find_all(name='title'))

# all_anchor_tags = soup.find_all(name='a')

# for tag in all_anchor_tags:
#     # tags = tag.getText()
#     # print(tags)
#     print(tag.get('href'))

# heading = soup.find(name='h1', id='name')
# print(heading.getText())

# section_heading = soup.find(name='h3', class_='heading')

# print(section_heading.get('class'))

# company_url = soup.select_one(selector='#name')

# print(company_url.getText())

# heading = soup.select('.heading')

# for h in heading:
#     print(h.getText())