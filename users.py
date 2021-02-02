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

driver.get('https://www.patreoncommunity.com/u?period=all')

# write a csv file for each of the companies
csv_file = open('user{0}.csv'.format(i), 'w', encoding='utf-8', newline='')
writer = csv.DictWriter(csv_file, 
                        fieldnames = ['username', 'fullName'. 'title', 'location', 'website',\
                            'bio', 'creatorType', 'patreonURL', 'joined', 'lastPosted', 'lastSeen',\
                            'views', 'invitedBy', 'trustLevel', 'daysVisited', 'readTime', 'recentReadTime',\
                            'topicsViewed', 'postsRead', 'likesGiven', 'topicsCreated', 'postsCreated',\
                            'likedReceived'])

# try to click on the load more button after scrolling all the way down continously until you cannot
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    try:
        # wait_button = WebDriverWait(driver, 10)
        # btn = wait_button.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="no-underline  show-more-reviews"]')))
        # btn.click()
        sleep(1.5)
        btn = driver.find_element_by_xpath('//a[@class="no-underline  show-more-reviews"]')
        btn.click()
    except:
        break
