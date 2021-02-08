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
                            'views', 'invitedBy', 'trustLevel', 'daysVisited', 'readTime',\
                            'recentReadTime', 'topicsViewed', 'postsRead', 'likesGiven',\
                            'topicsCreated', 'postsCreated', 'likesReceived'])
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
    try:
        creatorType = driver.find_element_by_xpath('.//*/div[@class="public-user-field creator-type-"]/span[@class="user-field-value"]').text
    except:
        creatorType = np.nan
    try:
        patreonURL = driver.find_element_by_xpath('.//*/div[@class="public-user-field patreon-url"]/span[@class="user-field-value"]').text
    except:
        patreonURL = np.nan
    
    detailStats1 = driver.find_elements_by_xpath('.//*/section[@class=" about has-background"]/div[@class="details"]/div[@class="secondary"]/dl/div')
    detailStats2 = driver.find_elements_by_xpath('.//*/section[@class=" about no-background"]/div[@class="details"]/div[@class="secondary"]/dl/div')
    # detailStats = driver.find_elements_by_xpath('''.//*/section[@class="(' about has-background' or ' about no-background']/div[@class="details"]/div[@class="secondary"]/dl/div''')
    for element in detailStats1:
        # the name of the variable we're going to scrape
        elementName = element.find_element_by_xpath('.//dt').text
        # print(elementName)

        if elementName == 'Joined':
            try:
                # joined = detailStats[0].find_element_by_xpath('.//dd/span').get_attribute('title')
                joined = element.find_element_by_xpath('.//dd/span').get_attribute('title')
            except:
                joined = np.nan
        elif elementName == 'Last Post':
            try:
                lastPosted = element.find_element_by_xpath('.//dd/span').get_attribute('title')
            except:
                lastPosted = np.nan
        elif elementName == 'Seen':
            try:
                lastSeen = element.find_element_by_xpath('.//dd/span').get_attribute('title')
            except:
                lastSeen = np.nan
        elif elementName == 'Views':
            try:
                views = element.find_element_by_xpath('.//dd').text
            except:
                views = np.nan
        elif elementName == 'Invited By':
            try:
                invitedBy = element.find_element_by_xpath('.//dd/a').text
            except:
                invitedBy = np.nan
        elif elementName == 'Trust Level':
            try:
                trustLevel = element.find_element_by_xpath('.//dd').text
            except:
                trustLevel = np.nan
        else:
            continue
    
    for element in detailStats2:
        # the name of the variable we're going to scrape
        elementName = element.find_element_by_xpath('.//dt').text
        # print(elementName)

        if elementName == 'Joined':
            try:
                # joined = detailStats[0].find_element_by_xpath('.//dd/span').get_attribute('title')
                joined = element.find_element_by_xpath('.//dd/span').get_attribute('title')
            except:
                joined = np.nan
        elif elementName == 'Last Post':
            try:
                lastPosted = element.find_element_by_xpath('.//dd/span').get_attribute('title')
            except:
                lastPosted = np.nan
        elif elementName == 'Seen':
            try:
                lastSeen = element.find_element_by_xpath('.//dd/span').get_attribute('title')
            except:
                lastSeen = np.nan
        elif elementName == 'Views':
            try:
                views = element.find_element_by_xpath('.//dd').text
            except:
                views = np.nan
        elif elementName == 'Invited By':
            try:
                invitedBy = element.find_element_by_xpath('.//dd/a').text
            except:
                invitedBy = np.nan
        elif elementName == 'Trust Level':
            try:
                trustLevel = element.find_element_by_xpath('.//dd').text
            except:
                trustLevel = np.nan
        else:
            continue

    
    userStats = driver.find_elements_by_xpath('.//*/div[@class="user-content-wrapper"]/div[@class="user-content"]/div[@class="top-section stats-section"]/ul/li')
    # print(len(userStats))
    for element in userStats:
        # the name of the variable we're going to scrape
        elementName = element.find_element_by_xpath('.//div/span[@class="label"]').text
        # print(elementName)
        
        if elementName == 'days visited':
            try:
                daysVisited = element.find_element_by_xpath('.//span[@class="value"]/span').text
            except:
                daysVisited = np.nan
        elif elementName == 'read time':
            try:
                readTime = element.find_element_by_xpath('.//dd/span').get_attribute('title')
            except:
                readTime = np.nan
        elif elementName == 'recent read time':
            try:
                recentReadTime = element.find_element_by_xpath('.//dd/span').get_attribute('title')
            except:
                recentReadTime = np.nan
        elif elementName == 'topics viewed':
            try:
                topicsViewed = element.find_element_by_xpath('.//dd/span').get_attribute('title')
            except:
                topicsViewed = np.nan
        elif elementName == 'posts read':
            try:
                postsRead = element.find_element_by_xpath('.//dd/span').get_attribute('title')
            except:
                postsRead = np.nan
        elif elementName == 'given':
            try:
                likesGiven = element.find_element_by_xpath('.//dd/span').get_attribute('title')
            except:
                likesGiven = np.nan
        elif elementName == 'topics created':
            try:
                topicsCreated = element.find_element_by_xpath('.//dd/span').get_attribute('title')
            except:
                topicsCreated = np.nan
        elif elementName == 'posts created':
            try:
                postsCreated = element.find_element_by_xpath('.//dd/span').get_attribute('title')
            except:
                postsCreated = np.nan
        elif elementName == 'received':
            try:
                likesReceived = element.find_element_by_xpath('.//dd/span').get_attribute('title')
            except:
                likesReceived = np.nan
    
    # try:
    #     daysVisited = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    # except:
    #     daysVisited = np.nan
    # try:
    #     readTime = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    # except:
    #     readTime = np.nan
    # try: # some people don't have a recent read time
    #     recentReadTime = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    # except:
    #     recentReadTime = np.nan
    # try:
    #     topicsViewed = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    # except:
    #     topicsViewed = np.nan
    # try:
    #     postsRead = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    # except:
    #     postsRead = np.nan
    # try:
    #     likesGiven = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    # except:
    #     likesGiven = np.nan
    # try:
    #     topicsCreated = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    # except:
    #     topicsCreated = np.nan
    # try:
    #     postsCreated = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    # except:
    #     postsCreated = np.nan
    # try:
    #     likesReceived = driver.find_element_by_xpath('.//*/div[@class="bio"]/div[@id="ember19"]/p').text
    # except:
    #     likesReceived = np.nan

    userDict = {}

    userDict['username'] = username
    userDict['fullName'] = fullName
    userDict['title'] = title
    userDict['location'] = location
    userDict['website'] = website
    userDict['bio'] = bio
    userDict['creatorType'] = creatorType
    userDict['patreonURL'] = patreonURL
    userDict['joined'] = joined
    userDict['lastPosted'] = lastPosted
    userDict['lastSeen'] = lastSeen
    userDict['views'] = views
    userDict['invitedBy'] = invitedBy
    userDict['trustLevel'] = trustLevel
    userDict['daysVisited'] = daysVisited
    # userDict['readTime'] = readTime
    # userDict['recentReadTime'] = recentReadTime
    # userDict['topicsViewed'] = topicsViewed
    # userDict['postsRead'] = postsRead
    # userDict['likesGiven'] = likesGiven
    # userDict['topicsCreated'] = topicsCreated
    # userDict['postsCreated'] = postsCreated
    # userDict['likesReceived'] = likesReceived

    writer.writerow(userDict)

    driver.quit()


# # scroll down to the very bottom of the page
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
