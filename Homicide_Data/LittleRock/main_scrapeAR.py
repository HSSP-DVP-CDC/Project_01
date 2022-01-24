#Little Rock, Arkansas

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
os.remove("/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Data_Sets/Little_Rock_Police_Department_Statistics_2017_to_Year_to_Date.csv")
print("Dataset deleted and ready to be replaced")

#Set Chrome Options
options = Options()
options.add_argument('--headless')
prefs = {"download.default_directory":"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Data_Sets"}
options.add_experimental_option('prefs', prefs)

#Set Chrome Driver 
chrome_path = r"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/chromedriver"
driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.implicitly_wait(10)

#Fetch webpage data
driver.get("https://lrstat.littlerock.gov/Safe-City/Little-Rock-Police-Department-Statistic-Insights/9iy3-rb7k")

#Button to click filter by homicide
filt_homicide = driver.find_element(By.XPATH, "//*[@id='card-container']/div[2]/card/div[2]/column-chart/div/div/div[2]/div[1]/div[12]/div[1]")
filt_homicide.click()
print("Filter clicked")

sleep (10)

#Button to export current rows
export_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/info-pane/div/div[2]/div/export-menu/div/button[1]") 
export_button.click()
print("Export clicked")

sleep(10)

#Button to change to only select current filter
currentfilt_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/info-pane/div/div[2]/div/export-menu/div/div/div/div[2]/div/span[2]/label/input")
currentfilt_button.click()
print("Change to current filter")

sleep(10)

#Button to download the relevant data
dwnload = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/info-pane/div/div[2]/div/export-menu/div/div/div/div[2]/a")
dwnload.click()
print("Download relevant data")

sleep(120)
print("Sleep complete")

#Close browser window when complete
driver.close()
print("Driver closed")

#Read .csv file
df = pd.read_csv('Data_Sets/Little_Rock_Police_Department_Statistics_2017_to_Year_to_Date.csv')
# print(df)

# Sort the data
sorted_df = df.sort_values(by=["INCIDENT_DATE"], ascending=False)

#Create new dataframe
sorted_df.to_csv('Data_Sets/arkansas_homicide_sorted.csv', index=False)

df = pd.read_csv("Data_Sets/arkansas_homicide_sorted.csv")
# print(df)

# 2022 
#Grab only values that are '09A' or 'Murder' for 2022
contains_values = df[df['INCIDENT_DATE'].str.contains('2022')]
print(contains_values)

#Create new dataframe
contains_values.to_csv('Data_Sets/arkansas_homicide_2022.csv', index=False)

df = pd.read_csv("Data_Sets/arkansas_homicide_2022.csv")
print(df)

print("Program complete")