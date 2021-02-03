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
    try:
        title = driver.find_element_by_xpath('.//*/div[@class="user-profile-names"]/h3').text
    except:
        title = np.nan
    try:
        location = driver.find_element_by_xpath('.//*/div[@class="user-profile-location"]').text
    except:
        location = np.nan
    try:
        website = driver.find_element_by_xpath('.//*/div[@class="user-profile-website"]/a').get_attribute('href')
    except:
        website = np.nan
    try:
        bio = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        bio = np.nan

    # left off
    try:
        creatorType = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        creatorType = np.nan
    try:
        patreonURL = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        patreonURL = np.nan
    try:
        joined = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        joined = np.nan
    try:
        lastPosted = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        lastPosted = np.nan
    try:
        lastSeen = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        lastSeen = np.nan
    try:
        views = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        views = np.nan
    try:
        invitedBy = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        invitedBy = np.nan
    try:
        trustLevel = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        trustLevel = np.nan
    try:
        daysVisited = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        daysVisited = np.nan
    try:
        readTime = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        readTime = np.nan
    try:
        recentReadTime = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        recentReadTime = np.nan
    try:
        topicsViewed = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        topicsViewed = np.nan
    try:
        postsRead = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        postsRead = np.nan
    try:
        likesGiven = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        likesGiven = np.nan
    try:
        topicsCreated = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        topicsCreated = np.nan
    try:
        postsCreated = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        postsCreated = np.nan
    try:
        likesReceived = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    except:
        likesReceived = np.nan

    userDict = {}

    userDict['username'] = username
    userDict['fullName'] = fullName
    userDict['title'] = title
    userDict['location'] = location
    userDict['website'] = website
    userDict['bio'] = bio

    writer.writerow(userDict)

    driver.quit()


# # scroll down to the very bottom of the page
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
