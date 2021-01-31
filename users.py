from selenium import webdriver
import re
import csv

chromeOptions = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images':2}
chromeOptions.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)

