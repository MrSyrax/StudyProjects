from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from creds import *
import time

#initial setup
USER = USER_NAME
PASSW = PASSWORD
chrome_driver_path = "c:/Development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://www.instagram.com/')
time.sleep(2)
user_name_input = driver.find_element(By.NAME, 'username')
pw_input = driver.find_element(By.NAME, 'password')
time.sleep(2)
user_name_input.send_keys(USER)
pw_input.send_keys(PASSW)
pw_input.send_keys(Keys.ENTER)
time.sleep(3)
driver.get('https://www.instagram.com/coders.learning/')
time.sleep(4)
followers_link = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[2]/a')
followers_link.click()
time.sleep(3)
follow_list_button = driver.find_elements(By.CSS_SELECTOR, 'li button')
for button in follow_list_button:
    try:
        button.click()
        time.sleep(1)
    except ElementClickInterceptedException:
        cancel_button = driver.find_element(By.XPATH,'/html/body/div[7]/div/div/div/div[3]/button[2]')
        cancel_button.click()

