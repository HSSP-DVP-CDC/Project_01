#Florida

#Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 
import pandas as pd

#Set Chrome Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
prefs = {"download.default_directory":"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Florida"}
options.add_experimental_option('prefs', prefs)

#Set Chrome Driver 
chrome_path = r"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/chromedriver"
# driver = webdriver.Chrome(chrome_path)
driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.implicitly_wait(10)

#Fetch webpage data
driver.get("https://transparency.jaxsheriff.org/HOTS/Murder")

print("Hello")

#Close browser window when complete
driver.close()