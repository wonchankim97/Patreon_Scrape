from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import re
import numpy as np
import csv

# read in all the users into a list that we'll loop
with open('users.csv', 'r') as f:
    users = f.readlines()
    users = list(map(lambda x: x.strip('\n'), users))

# write a csv file with each user as a row
csv_file = open('userData.csv', 'w', encoding='utf-8', newline='')
writer = csv.DictWriter(csv_file, 
                        fieldnames = ['username', 'fullName', 'title', 'location', 'website',\
                            'bio', 'creatorType', 'patreonURL', 'joined', 'lastPosted', 'lastSeen',\
                            'views', 'invitedBy', 'trustLevel', 'daysVisited', 'readTime', 'recentReadTime',\
                            'topicsViewed', 'postsRead', 'likesGiven', 'topicsCreated', 'postsCreated',\
                            'likesReceived'])
writer.writeheader()

for i in range(len(users[:3])):
    # open up a driver for each user page
    chromeOptions = webdriver.ChromeOptions()
    prefs = {'profile.managed_default_content_settings.images':2}
    chromeOptions.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=chromeOptions)
    
    driver.get(users[i])
    
    try:
        username = driver.find_element_by_xpath('.//*/h1[@class="username"]').text
    except:
        username = np.nan
    try:
        fullName = driver.find_element_by_xpath('.//*/h2[@class="full-name"]').text
    except:
        fullName = np.nan

    userDict = {}

    userDict['username'] = username
    userDict['fullName'] = fullName

    writer.writerow(userDict)

    driver.quit()


# # scroll down to the very bottom of the page
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
