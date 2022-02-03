#Louisville, Kentucky

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
os.remove("/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Data_Sets/2022/CRIME_DATA_2022.csv")
print("Dataset deleted and ready to be replaced")

#Set Chrome Options
options = Options()
options.add_argument('--headless')
prefs = {"download.default_directory":"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Data_Sets/2022"}
options.add_experimental_option('prefs', prefs)

#Set Chrome Driver 
chrome_path = r"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/chromedriver"
driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.implicitly_wait(10)

#Fetch webpage data
driver.get("https://data.louisvilleky.gov/dataset/crime-reports")

dwnload = driver.find_element(By.XPATH, "//*[@id='data-and-resources']/div/div/ul/li[1]/div/span/a")
dwnload.click()
print("Download initiated")

sleep(180)
print("Sleep complete")

#Close browser window when complete
driver.close()
print("Driver closed")

#Read .csv file
df = pd.read_csv('/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Data_Sets/2022/CRIME_DATA_2022.csv')
# print(df)

# Sort the data
sorted_df = df.sort_values(by=["DATE_REPORTED"], ascending=False)

#Create new dataframe
sorted_df.to_csv('/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Data_Sets/2022/kentucky_homicide_sorted.csv', index=False)

df = pd.read_csv("/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Data_Sets/2022/kentucky_homicide_sorted.csv")
# print(df)

#Grab only values that are '09A' or 'Murder'
contain_values = sorted_df[sorted_df['NIBRS_CODE'].str.contains('09A')]
print(contain_values)

#Create new dataframe
contain_values.to_csv('/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Data_Sets/2022/kentucky_homicide_09A.csv', index=False)

df = pd.read_csv("/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Data_Sets/2022/kentucky_homicide_09A.csv")
print(df)

print("Program complete")