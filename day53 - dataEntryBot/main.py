from os import name
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from credentials import *
from pprint import pp, pprint
import pandas
import requests
import time

#links
# CHROME_DRIVER_PATH = "c:/Development/chromedriver.exe"
# URL_FOR_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSdkpM0XsHCaZZzYSTgmLa3w1e0DnCkCmI7qi6sJ_RIp6rKOZQ/viewform'
URL_FOR_ZILLOW = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
# URL_FOR_DOCS = 'https://docs.google.com/forms/u/0/'
# URL_FOR_RESPONSES = 'https://docs.google.com/forms/d/1VkJT4lS3KcI5ghauHEGk8k-HYIr9wq9ZHPzXHMbL6U8/edit#responses'
# USER = USER_NAME
# PASSWORD = PASS

# driver = webdriver.Chrome(CHROME_DRIVER_PATH)

# def log_into_docs():
#     driver.get(URL_FOR_DOCS)
#     docs_login_email = driver.find_element(By.ID, "identifierId")
#     docs_login_email.send_keys(USER)
#     docs_login_email.send_keys(Keys.ENTER)
#     time.sleep(2)
#     pass_field = driver.find_element(By.NAME, 'password')
#     pass_field.send_keys(PASSWORD)

# log_into_docs()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'Accepted-Language': 'en-US,en;q=0.9'
}

response = requests.get(URL_FOR_ZILLOW, headers=headers)
funsies = response.text
soup = BeautifulSoup(funsies, 'html.parser')
links = soup.select(".list-card-top a")
for l in links:
    print(l)