from types import CellType
import requests
from decouple import config
import json
from datetime import datetime as dt
from requests.api import head
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stocks_api_k = config('KEY_FOR_STOCKS')
news_api_k = config('KEY_FOR_NEWS')
twilio_key = config('auth_token')
twilio_sid = config('account_sid')
client = Client(twilio_sid,twilio_key)
news_endpoint = 'https://newsapi.org/v2/everything'
headline = []
brief = []


parameters_stocks = {
    'function':'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey':stocks_api_k
}


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
url = 'https://www.alphavantage.co/query'
data = requests.get(url, params=parameters_stocks)
data.raise_for_status()

stock_data = data.json()['Time Series (Daily)']
stock_data_list = [value for (key,value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterady_closing_price = yesterday_data['4. close']
day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

difference = abs(float(yesterady_closing_price) - float(day_before_yesterday_closing_price))
difference_percet = (difference/float(yesterady_closing_price))*100

news_params = {
    'apiKey':news_api_k,
    'qInTitle': COMPANY_NAME
}

news = requests.get(news_endpoint, params=news_params)
articles = news.json()['articles'][:3]
msg = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in articles]


if difference_percet > 3:
    news = requests.get(news_endpoint, params=news_params)
    articles = news.json()['articles'][:3]
    msg = [f"TSLA:🔺{round(difference_percet, 2)}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in articles]
    message = client.messages.create(body=msg, from_='+12565988358',to='+17145925544')

elif difference_percet < 3:
    news = requests.get(news_endpoint, params=news_params)
    articles = news.json()['articles'][:3]

    title = [n['title'] for n in articles]
    description = [n['description'] for n in articles]
    message = f'TSLA: 🔻 {round(difference_percet, 2)}%\nHeadline: {title[0]}\nBrief: {description[0]}'
    msg = client.messages.create(body=message,from_='+12565988358',to='+17145925544')


#🔻
#🔺

