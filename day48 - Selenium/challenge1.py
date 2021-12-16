from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#initial setup
chrome_driver_path = "c:/Development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#set timer values
#set 5 second timer
check_timer = time.time() + 3
#set 5 minute time out mechanism
time_out = time.time() + 60 * 5

#get static values
#grab the cookie to click on
cookie_to_click = driver.find_element(By.ID, 'cookie')
#grab the list of divs that hold the upgrades
store_upgrades = driver.find_elements(By.CSS_SELECTOR, '#store div')
#list comp to get the id attribute from each div "buyCursor","buyGrandma"...etc
item_ids = [item.get_attribute('id') for item in store_upgrades]


while True:
   cookie_to_click.click()

   if time.time() > check_timer:
      #grab all of the prices, you have to pull it in the while loop
      #because there is a hidden upgrade that will show up randomly
      all_prices = driver.find_elements(By.CSS_SELECTOR, '#store b')
      cost=[]
      for price in all_prices:
         element_text = price.text
         #because there is a hidden upgrade one of the items in the list will 
         #be blank so we need an if check
         if element_text != '':
            #use .split to remove the - between the price
            #use .strip to remove the spaces on the sides
            #use .replace to remove the commas for larger numbers EX:1,000 = 1000
            cost.append(int(price.text.split('-')[1].strip().replace(',','')))
      
      #creat a dictuonary of the cost + item ids
      cookie_upgrades = {}
      #for the current number in the range of the length of cost(which is a list)
      for n in range(len(cost)):
         #add the cost at index n and make the value = index n from item_id's list
         cookie_upgrades[cost[n]]=item_ids[n]

      #grab the current cookie count
      money_element = driver.find_element(By.ID, 'money').text
      #check if there is a comma in the current money element 
      if ',' in money_element:
         #if there is remove the comma using .replace(',','')
         money_element = money_element.replace(',','')
         #conver money_element to int and store it in cookie_count
      cookie_count = int(money_element)
      
      #find the upgrade we can currently afford
      affordable_upgrades = {}
      #for every cost and id in cookie_upgrades dictionary
      for cost, id in cookie_upgrades.items():
         #check if the current cookie count is greater than the cost
         if cookie_count > cost:
            #if it is then make add that cost and id to the 
            #affordable_upgarades dict as cost:id
            affordable_upgrades[cost]=id
      
      #purchase the most expensive upgrade we can afford.
      highest_price_affordable = max(affordable_upgrades)
      print(highest_price_affordable)
      #grab the id of the most expensive upgrade we can afford 
      #from affordable_upgrades
      to_purchase_id = affordable_upgrades[highest_price_affordable]

      driver.find_element(By.ID, to_purchase_id).click()

      #add 5 sec to check timer
      check_timer = time.time() + 5

   if time.time() > time_out:
      cookie_per_sec = driver.find_element(By.ID,'cps').text
      print(cookie_per_sec)
      break

driver.quit()



      







