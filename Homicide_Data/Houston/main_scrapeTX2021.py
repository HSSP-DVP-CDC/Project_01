#Texas, Houston
#Scapes into a MASTER FOLDER

#Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time 
from time import sleep
import pandas as pd
import os

#Delete current file to prevent duplication of datasets
os.remove("/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Data_Sets/2021/NIBRSPublicViewDec21.xlsx")
os.remove("/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Data_Sets/2021/NIBRSPublicViewDec21.csv")
print("Datasets deleted and ready to be replaced")
 
#Set Chrome Options
options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument("--disable-extensions")
prefs = {"download.default_directory":"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Data_Sets/2021"}
options.add_experimental_option('prefs', prefs)

#Set Chrome Driver 
chrome_path = r"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/chromedriver"
driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.implicitly_wait(10)

#Fetch webpage data
driver.get("https://www.houstontx.gov/police/cs/Monthly_Crime_Data_by_Street_and_Police_Beat.htm")

dwnload = driver.find_element(By.XPATH, "//*[@id='main']/div[1]/div[3]/div[1]/p[2]/a")
dwnload.click()

sleep(180)
print("Sleep complete")

# #Close browser window when complete
driver.close()
print("Driver closed")

# Through December 2021 Data
print("Data through December 2021")
read_file = pd.read_excel('Data_Sets/2021/NIBRSPublicViewDec21.xlsx')
read_file.to_csv("Data_Sets/2021/NIBRSPublicViewDec21.csv")

df = pd.read_csv("Data_Sets/2021/NIBRSPublicViewDec21.csv")
# print(df)

# Sort the data
sorted_df = df.sort_values(by=["RMSOccurrenceDate"], ascending=False)

#Create new dataframe
sorted_df.to_csv('Data_Sets/2021/texas_homicide_sorted.csv', index=False)

sorted_df = pd.read_csv("Data_Sets/2021/texas_homicide_sorted.csv")
# print(df)

#Grab only values that are '09A' or 'Murder'
contain_values = sorted_df[sorted_df['NIBRSClass'].str.contains('09A')]
print(contain_values)

#Create new dataframe
contain_values.to_csv('Data_Sets/2021/texas_homicide_09A.csv', index=False)

df = pd.read_csv("Data_Sets/2021/texas_homicide_09A.csv")
print(df)

print("Program complete")