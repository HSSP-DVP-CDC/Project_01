#Texas
#Houston

#Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 
from time import sleep
import pandas as pd
# import os, sys 

#Set Chrome Options
options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument("--disable-extensions")
prefs = {"download.default_directory":"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Houston"}
options.add_experimental_option('prefs', prefs)

#Set Chrome Driver 
chrome_path = r"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/chromedriver"
# driver = webdriver.Chrome(chrome_path)
driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.implicitly_wait(10)

#Fetch webpage data
driver.get("https://www.houstontx.gov/police/cs/Monthly_Crime_Data_by_Street_and_Police_Beat.htm")

dwnload = driver.find_element(By.XPATH, "//*[@id='main']/div[1]/div[3]/div[1]/p[2]/a")
dwnload.click()

sleep(180)

# #Close browser window when complete
driver.close()

#October Data
# print("Oct 2021")
# read_file = pd.read_excel('Homicide_Data/Houston/NIBRSPublicViewOct21.xlsx')
# read_file.to_csv("Homicide_Data/Houston/NIBRSPublicViewOct21.xlsx")

# df = pd.read_csv("Homicide_Data/Houston/NIBRSPublicViewOct21.xlsx")
# print(df)

# November Data
print("Nov 2021")
read_file = pd.read_excel('Homicide_Data/Houston/NIBRSPublicViewNov21.xlsx')
read_file.to_csv("Homicide_Data/Houston/NIBRSPublicViewNov21.xlsx")

df = pd.read_csv("Homicide_Data/Houston/NIBRSPublicViewNov21.xlsx")
print(df)

# Sort the data
sorted_df = df.sort_values(by=["RMSOccurrenceDate"], ascending=False)

#Create new dataframe
sorted_df.to_csv('Homicide_Data/Houston/texas_homicide_sorted', index=False)

df = pd.read_csv("Homicide_Data/Houston/texas_homicide_sorted")
print(df)