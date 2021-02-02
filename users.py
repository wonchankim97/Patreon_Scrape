from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import re
import csv

chromeOptions = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images':2}
chromeOptions.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=chromeOptions)

driver.get('https://www.patreoncommunity.com/u?period=all') # https://www.patreoncommunity.com/

# write a csv file for all users
csv_file = open('users.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

# # use to test
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

########### SCROLL TO BOTTOM ###########
# scroll down to the very bottom of the page
lastHeight = driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# continuously scroll to get all users
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    # wait for page to load
    sleep(1)

    # Calculate new scroll height and compare with last scroll height
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight
########### SCROLL TO BOTTOM ###########

# get the xpath of the users
# users = driver.find_elements_by_xpath('//div[@class="loading-container ember-view"]') # driver.find_element_by_id("link")
users = driver.find_elements_by_xpath('//tr[@class="ember-view"]')

# loop through and get the links of each user
for user in users:
    # find the link
    userLink = user.find_element_by_xpath('.//*/span[@class="username"]/a').get_attribute('href')
    # write into csv
    writer.writerow([userLink])
    # print(userLink)
    # sleep(0.2)

driver.quit()