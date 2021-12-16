from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 75
PROMISED_UP = 10
CHROME_DRIVER_PATH = "c:/Development/chromedriver.exe"
TWITTER_EMAIL = 'kevinlearningpython@gmail.com'
TWITTER_PASSWORD = '5925544Kk!!'

class InternetSpeedTwitterBot:
    def __init__(self, driverpath):
        self.driver = webdriver.Chrome(driverpath)
        self.down = 0
        self.up = 0
      

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(2)
        button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        time.sleep(2)
        button.click()
        time.sleep(80)
        self.down = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self, tweet_to_send_out):
        self.driver.get('https://twitter.com/login')
        time.sleep(5)
        email_input = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)
        time.sleep(5)
        pass_word_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass_word_input.send_keys(TWITTER_PASSWORD)
        pass_word_input.send_keys(Keys.ENTER)
        time.sleep(5)
        text_box = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        text_box.send_keys(tweet_to_send_out)
        tweet_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
down_speed = bot.down
up_speed = bot.up
tweet = f'@itswolv3 Why is my internet so slow?\nDownload speed was: {down_speed}Mbps\nUpload speed was: {up_speed}Mbps'
bot.tweet_at_provider(tweet)

bot.driver.quit()