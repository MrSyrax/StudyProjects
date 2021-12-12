import requests
import lxml
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Steelcase-Gesture-Office-Connect-Licorice/dp/B08LN39FH5/ref=sr_1_3_sspa?crid=3PN0PGQIBDMXE&keywords=steelcase+leap&qid=1639223449&sprefix=steelcase%2Caps%2C232&sr=8-3-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFYUUVOTEZJWU5HVEkmZW5jcnlwdGVkSWQ9QTA5NTI4NzUyS0JTTjJVSzNBMlhTJmVuY3J5cHRlZEFkSWQ9QTA4ODY5MDYyVldSUTY4WFQ4VzBTJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'Accepted-Language': 'en-US,en;q=0.9'
}

response = requests.get(URL, headers=headers)

chair_page = response.content
soup = BeautifulSoup(chair_page, 'lxml')

chair_ratings_container = soup.find(id='bylineInfo')

chair_ratings_link = chair_ratings_container.get('href')

link = f'https://www.amazon.com{chair_ratings_link}'
print(link)

chair_price_container = soup.find(id='corePrice_desktop')
print(chair_price_container.span.span.get_text())

