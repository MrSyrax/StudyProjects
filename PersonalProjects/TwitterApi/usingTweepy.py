from requests_oauthlib import OAuth1Session
from credentials import Credentials
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# In your terminal please set your environment variables by running the following lines of code.
# export 'CONSUMER_KEY'='<your_consumer_key>'
# export 'CONSUMER_SECRET'='<your_consumer_secret>'



consumer_key = Credentials.api_key
consumer_secret = Credentials.api_secret
UN = Credentials.user_name1
UN2 = Credentials.user_name2
PW = Credentials.pass_word

# Be sure to add replace the text of the with the text you wish to Tweet. You can also add parameters to post polls, quote Tweets, Tweet with reply settings, and Tweet to Super Followers in addition to other features.
print('What did you learn today?')
tweet = input()
payload = {"text": f"Today I learned {tweet}"}

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "There may have been an issue with the consumer_key or consumer_secret you entered."
    )

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)
# Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
time.sleep(5)
driver_path = "c:/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(authorization_url)
time.sleep(4)
user_name = driver.find_element(By.XPATH, '//*[@id="username_or_email"]')
user_name.send_keys(UN)
pass_word = driver.find_element(By.XPATH, '//*[@id="password"]')
pass_word.send_keys(PW)
button_to_click = driver.find_element(By.XPATH, '//*[@id="allow"]')
button_to_click.click()
time.sleep(4)
# user_name2 = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
# user_name2.send_keys(UN)
# user_name2.send_keys(Keys.ENTER)
# time.sleep(4)
# user_name3 = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
# user_name3.send_keys(UN2)
# user_name3.send_keys(Keys.ENTER)
# time.sleep(3)
# pass_word2 = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
# pass_word2.send_keys(PW)
# pass_word2.send_keys(Keys.ENTER)
# time.sleep(3)
# auth_button = driver.find_element(By.XPATH,'//*[@id="allow"]')
# auth_button.click()
# time.sleep(2)
auth_key = driver.find_element(By.XPATH,'//*[@id="oauth_pin"]/p/kbd/code')
print("Please go here and authorize: %s" % authorization_url)
verifier = auth_key.text

# Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

# Making the request
response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

if response.status_code != 201:
    raise Exception(
        f"Request returned an error: {response.status_code} {response.text}"
    )

print(f"Response code: {response.status_code}")

# Saving the response as JSON
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))