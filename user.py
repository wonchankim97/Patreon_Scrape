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

for i in range(len(users[:3])):
    # write a csv file for each user
    csv_file = open('user{0}.csv'.format(i), 'w', encoding='utf-8', newline='')
    writer = csv.DictWriter(csv_file, 
                            fieldnames = ['username', 'fullName'. 'title', 'location', 'website',\
                                'bio', 'creatorType', 'patreonURL', 'joined', 'lastPosted', 'lastSeen',\
                                'views', 'invitedBy', 'trustLevel', 'daysVisited', 'readTime', 'recentReadTime',\
                                'topicsViewed', 'postsRead', 'likesGiven', 'topicsCreated', 'postsCreated',\
                                'likedReceived'])

    # open up a driver for each user page
    chromeOptions = webdriver.ChromeOptions()
    prefs = {'profile.managed_default_content_settings.images':2}
    chromeOptions.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=chromeOptions)

    username = 


# # scroll down to the very bottom of the page
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
