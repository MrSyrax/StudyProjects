from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time


email_login ='kevincarrillo89@gmail.com'
password_login = '5426233Kk!!'

web_driver_path = "c:/Development/chromedriver.exe"
driver = webdriver.Chrome(web_driver_path)
driver.get('https://tinder.com/')

time.sleep(2)
log_in_button = driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in_button.click()
time.sleep(2)
fb_sign_in_button = driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_sign_in_button.click()
time.sleep(2)

window_base = driver.window_handles[0]
fb_window_handle = driver.window_handles[1]
driver.switch_to.window(fb_window_handle)

time.sleep(1)
email = driver.find_element(By.ID, 'email')
pass_word = driver.find_element(By.ID, 'pass')
email.send_keys(email_login)
pass_word.send_keys(password_login)
login_button = driver.find_element(By.NAME, 'login')
login_button.click()

time.sleep(2)
driver.switch_to.window(window_base)

time.sleep(10)
# location_button = driver.find_element(By.XPATH,'//*[@id="o-1335420887"]/div/div/div/div/div[3]/button[1]')
# location_button.click()
# time.sleep(2)
# notifications_button = driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div/div/div[3]/button[1]')
# notifications_button.click()
# time.sleep(2)
decline_button = driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
for n in range(100):
    try:
        time.sleep(2)
        decline_button.click()
        
    except ElementClickInterceptedException:
        try:
            match_pop_up = driver.find_element(By.CSS_SELECTOR,'.itsAMatch a')
            match_pop_up.click()
        except NoSuchElementException:
            time.sleep(2)


driver.quit()

4


