from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "c:/Development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&f_WT=2&geoId=103644278&keywords=python%20developer&location=United%20States&sortBy=R')
U_NAME = config('U_NAME')
P_W = config('P_W')

log_in_button = driver.find_element(By.CLASS_NAME,'nav__button-secondary')
log_in_button.click()
time.sleep(1)
user_name_entry = driver.find_element(By.ID,'username')
user_name_entry.send_keys(U_NAME)
pass_entry = driver.find_element(By.ID, 'password')
pass_entry.send_keys(P_W)
time.sleep(1)
sign_in_button = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()


