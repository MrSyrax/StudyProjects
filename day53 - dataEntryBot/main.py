from os import link, name
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
CHROME_DRIVER_PATH = "c:/Development/chromedriver.exe"
URL_FOR_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSdkpM0XsHCaZZzYSTgmLa3w1e0DnCkCmI7qi6sJ_RIp6rKOZQ/viewform?usp=sf_link'
URL_FOR_ZILLOW = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'


#header is required for bypassing captcha
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'Accepted-Language': 'en-US,en;q=0.9'
}

#grab the page using requests
response = requests.get(URL_FOR_ZILLOW, headers=headers)
#assign the response.text to a variable
funsies = response.text
#create soup from that page using beautiful soup
soup = BeautifulSoup(funsies, 'html.parser')

#grab all of the links in the zillow page
links = soup.select(".list-card-top a")
#create a list to hold all of the links after edited in the following for loop
link_list = []
#create a for loop to go grab each link
for l in links:
#grab each link from the list of links
    ls = l.get('href')
#if the link doesn't start with 'https://' 
    if 'https://' not in ls:
# add 'https://www.zillow.com' to the start of it
        link_list.append('https://www.zillow.com'+ ls)
# if it inlcudes https:// already just add it to the list
    else:
        link_list.append(ls) 


#grab all of the addresses from zillow
all_addresses = soup.select(".list-card-info address")
#grab all of the text from the element
all_addresses_list = [address.text for address in all_addresses]

#grab all of the monthly prices from zillow
all_monthly_prices = soup.select('.list-card-price')
#go through the list of monthly prices and grab the text
all_monthly_prices_list = [price.text for price in all_monthly_prices]

clean_price_list = []
#clean up the monthly prices
for prices in all_monthly_prices_list:
   if '/' in prices:
       clean_price_list.append(prices.split('/')[0])
   elif '+' in prices:
       clean_price_list.append(prices.split('+')[0])

#create the webdriver with the chrome driver and store it in the variable "driver"
driver = webdriver.Chrome(CHROME_DRIVER_PATH)
for n in range(len(link_list)):
    #grab the google form to fill out
    driver.get(URL_FOR_FORM)
    #Delay before taking next actions as the page will load
    time.sleep(2)
    #grab the adress input
    form_address = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    #grab the price per month input
    form_price_month = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    #grab the link to property field
    form_link_to_property = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    #grab the button from the form
    form_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    form_address.send_keys(all_addresses_list[n])
    form_price_month.send_keys(clean_price_list[n])
    form_link_to_property.send_keys(link_list[n])
    form_button.click()

driver.quit()
