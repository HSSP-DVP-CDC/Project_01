#Louisville
#Kentucky

#Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 
from time import sleep
import pandas as pd

#Set Chrome Options
options = Options()
options.add_argument('--headless')
prefs = {"download.default_directory":"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Louisville"}
options.add_experimental_option('prefs', prefs)

#Set Chrome Driver 
chrome_path = r"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/chromedriver"
driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.implicitly_wait(10)

#Fetch webpage data
driver.get("https://data.louisvilleky.gov/dataset/crime-reports")

dwnload = driver.find_element(By.XPATH, "//*[@id='data-and-resources']/div/div/ul/li[1]/div/span/a")
dwnload.click()

sleep(180)

#Close browser window when complete
driver.close()

#Read .csv file
df = pd.read_csv('Homicide_Data/Louisville/CRIME_DATA_2021.csv')
print(df)

# Sort the data
sorted_df = df.sort_values(by=["DATE_REPORTED"], ascending=False)

#Create new dataframe
sorted_df.to_csv('Homicide_Data/Louisville/kentucky_homicide_sorted.csv', index=False)

df = pd.read_csv("Homicide_Data/Louisville/kentucky_homicide_sorted.csv")
print(df)

#Grab only values that are '09A' or 'Murder'
contain_values = df[df['NIBRS_CODE'].str.contains('09A')]
print(contain_values)

#Create new dataframe
contain_values.to_csv('Homicide_Data/Louisville/kentucky_homicide_09A.csv', index=False)

df = pd.read_csv("Homicide_Data/Louisville/kentucky_homicide_09A.csv")
print(df)