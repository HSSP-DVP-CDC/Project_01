#Detroit, Michigan
#Requires a pip install <arcgis> API to address login credentials during automated testing
#Source: https://developers.arcgis.com/python/guide/working-with-different-authentication-schemes/
#Helpful StackOverflow about working with shadowroots: https://stackoverflow.com/questions/68909696/clicking-side-panel-elements-in-selenium-without-iframes

#Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import time 
from time import sleep
import pandas as pd
import arcgis 
from arcgis.gis import GIS

#Set Chrome Options
options = Options()
# options.add_argument('--headless')
prefs = {"download.default_directory":"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Detroit"}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#Set Chrome Driver 
chrome_path = r"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/chromedriver"
driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.implicitly_wait(10)

#Fetch webpage data (already filtered by 'Homicide/Non-Negligent Murder')
driver.get("https://data.detroitmi.gov/datasets/rms-crime-incidents/explore?filters=eyJjaGFyZ2VfZGVzY3JpcHRpb24iOlsiTVVSREVSIC8gTk9OLU5FR0xJR0VOVCBNQU5TTEFVR0hURVIgKFZPTFVOVEFSWSkiLCJNVVJERVIgLyBOT04tTkVHTElHRU5UIE1BTlNMQVVHSFRFUiAoVk9MVU5UQVJZKSAgICAgICAgICAgICAiXSwieWVhciI6WzIwMjAuOTcsMjAyMV19&location=42.348386%2C-83.007003%2C10.62&showTable=true")
wait = WebDriverWait(driver, 60)

#ARCGIS Authetication 
print("ArcGIS Online as anonymous user")    
gis = GIS()
print("Logged in as anonymous user to " + gis.properties.portalName)

sleep(15)

#Button to begin download options
dwnload_option = driver.find_element(By.XPATH, "//*[@id='ember111']/div/button[3]")
dwnload_option.click()
print("Download option initiated")

sleep(25)

#Button to toggle filter
toggle = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/calcite-switch")
toggle.click()
print("Toggle initiated")

sleep(15)

#Button to download csv
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#ember44'))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div > div > div:nth-child(1) > div > div > div:nth-child(6) > hub-download-card")))
driver.execute_script('document.querySelector("div > div > div:nth-child(6) > hub-download-card").shadowRoot.querySelector("calcite-card > div > calcite-dropdown > calcite-button").click()')

print("Downloading csv")

sleep(15)

#Button to select new data for download
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#ember44'))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div > div > div:nth-child(1) > div > div > div:nth-child(6) > hub-download-card")))
driver.execute_script('document.querySelector("div > div > div:nth-child(6) > hub-download-card").shadowRoot.querySelector("calcite-card > div > calcite-dropdown > calcite-dropdown-group > calcite-dropdown-item:nth-child(1)").shadowRoot.querySelector("div").click()')

print("Generate new download with latest data")

sleep(120)
print("Sleep complete")

#Close browser window when complete
driver.close() 
print("Driver closed")                               

# Read the csv into the console
df = pd.read_csv("Homicide_Data/Detroit/RMS_Crime_Incidents.csv")
print(df)

# Sort the data
sorted_df = df.sort_values(by=["incident_timestamp"], ascending=False)
print(sorted_df)

#Create new dataframe
sorted_df.to_csv('Homicide_Data/Detroit/detroit_homicide_sorted.csv', index=False)

df = pd.read_csv("Homicide_Data/Detroit/detroit_homicide_sorted.csv")
print(df)

print("Program complete")