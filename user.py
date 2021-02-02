from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import re
import numpy as np
import csv

chromeOptions = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images':2}
chromeOptions.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)

driver.get('https://www.patreoncommunity.com/u?period=all') # https://www.patreoncommunity.com/

# write a csv file for each user
csv_file = open('user{0}.csv'.format(i), 'w', encoding='utf-8', newline='')
writer = csv.DictWriter(csv_file, 
                        fieldnames = ['username', 'fullName'. 'title', 'location', 'website',\
                            'bio', 'creatorType', 'patreonURL', 'joined', 'lastPosted', 'lastSeen',\
                            'views', 'invitedBy', 'trustLevel', 'daysVisited', 'readTime', 'recentReadTime',\
                            'topicsViewed', 'postsRead', 'likesGiven', 'topicsCreated', 'postsCreated',\
                            'likedReceived'])

# # scroll down to the very bottom of the page
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
