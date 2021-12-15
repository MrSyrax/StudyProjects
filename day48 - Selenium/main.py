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


#-------------------------------------------------------------------------#

time = driver.find_elements(By.CSS_SELECTOR,'.event-widget time')
title = driver.find_elements(By.CSS_SELECTOR,'.event-widget li a')

events = {}
for n in range(len(time)):
    t = time[n].get_attribute('datetime')
    events[n] = {
        'time': t.split('T')[0],
        'name': title[n].text
    }


print(events)

#-----------------------------------------------------------------------#

driver.quit()

