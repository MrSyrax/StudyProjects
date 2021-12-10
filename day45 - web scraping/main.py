from bs4 import BeautifulSoup
import requests

url = 'https://news.ycombinator.com/'

response = requests.get(url)
yc_web_page = response.text

<<<<<<< HEAD
soup = BeautifulSoup(yc_web_page, 'html.parser')

titlelink = soup.find_all(name='a', class_='titlelink')
article_text = []
article_link = []
article_upvote = []


for line in titlelink:
    article_text.append(line.getText())
    article_link.append(line.get('href'))


article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]


# print(article_text)
# print(article_link)
# print(article_upvote)

max_upvote = max(article_upvote)
max_upvote_index = article_upvote.index(max_upvote)
top_article = article_text[max_upvote_index]
top_article_link = article_link[max_upvote_index]

print(top_article)
print(top_article_link)
print(max_upvote)



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
=======
print(soup.title)
print(soup.title.name)
>>>>>>> 4369aa48ff230be44f11d94a07ce3a1f83c958c8
