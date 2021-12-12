from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = 'c:/Development/chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")  

# search_box = driver.find_element(By.ID,"twotabsearchtextbox")
# search_box.send_keys('notebooks')

# div = driver.find_element(By.ID,'apex_desktop')
# span = div.find_elements(By.TAG_NAME, 'span')
# print(span[0].text)

# span = driver.find_element(By.CSS_SELECTOR,'#apex_desktop span')

# price = float(span.text.split('$')[1])


# #-------------------------------------------------------------------------#

time = driver.find_elements(By.CSS_SELECTOR,'.event-widget time')
title = driver.find_elements(By.CSS_SELECTOR,'.event-widget a')

events = {}
counter = 0
for times in time:
    x =times.get_attribute('datetime')
    events[counter]={'time': x.split('T')[0]}
    counter+=1


new_counter = 0  
for titles in title:
    if titles.text != 'More':
        events[new_counter]['name'] = titles.text
        new_counter+=1

print(events)

# #-----------------------------------------------------------------------#

driver.quit()