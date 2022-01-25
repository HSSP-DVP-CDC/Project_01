#Jacksonville, Florida
#Murder Data

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
os.remove("/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Data_Sets/Exported Data.csv")
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
driver.get("https://transparency.jaxsheriff.org/HOTS/Murder")

dwnload = driver.find_element(By.XPATH, "//*[@id='M_C_MainContent_MainContent_ecExport_hlExport']")
dwnload.click()

# Pause 10 seconds to allow CSV to download
sleep(10)
      
#Close browser window when complete
driver.close()
print("Program Complete.")

# Print the data fram
df = pd.read_csv("Data_Sets/Exported Data.csv")
# print(df)

# 2022 
#Grab only values that are '09A' or 'Murder' for 2022
contains_values = df[df['IncidentDate'].str.contains('2022')]
print(contains_values)

#Create new dataframe
contains_values.to_csv('Data_Sets/jacksonville_homicide_2022.csv', index=False)

df = pd.read_csv("Data_Sets/jacksonville_homicide_2022.csv")
print(df)

print("Program complete")