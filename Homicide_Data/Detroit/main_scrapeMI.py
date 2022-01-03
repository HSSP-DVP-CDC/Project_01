#Detroit
#Michigan
#Requires a pip install <arcgis> API to address login credentials during automated testing
#Source: https://developers.arcgis.com/python/guide/working-with-different-authentication-schemes/

#Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 
from time import sleep
import pandas as pd
import arcgis 
from arcgis.gis import GIS


#Set Chrome Options
options = Options()
#options.add_argument('--headless')
prefs = {"download.default_directory":"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Detroit"}
options.add_experimental_option('prefs', prefs)

#Set Chrome Driver 
chrome_path = r"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/chromedriver"
driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.implicitly_wait(10)

#Fetch webpage data (already filtered by 'Homicide/Non-Negligent Murder')
driver.get("https://data.detroitmi.gov/datasets/rms-crime-incidents/explore?filters=eyJjaGFyZ2VfZGVzY3JpcHRpb24iOlsiTVVSREVSIC8gTk9OLU5FR0xJR0VOVCBNQU5TTEFVR0hURVIgKFZPTFVOVEFSWSkiLCJNVVJERVIgLyBOT04tTkVHTElHRU5UIE1BTlNMQVVHSFRFUiAoVk9MVU5UQVJZKSAgICAgICAgICAgICAiXSwieWVhciI6WzIwMjAuOTcsMjAyMV19&location=42.348386%2C-83.007003%2C10.62&showTable=true")

#ARCGIS Authetication 
print("ArcGIS Online as anonymous user")    
gis = GIS()
print("Logged in as anonymous user to " + gis.properties.portalName)

sleep(15)

#Button to begin download options
dwnload_option = driver.find_element(By.XPATH, "//*[@id='ember111']/div/button[3]")
dwnload_option.click()
print("Download option initiated")

#Button to toggle filter
#filt_toggle = driver.find_element(By.XPATH, "//*[@id='ember44']/div/div/div[1]/div/div/div[2]/div/calcite-switch//div")
filt_toggle = driver.find_element(By.XPATH, "//*[@id='ember44']/div/div/div[1]/div/div/div[2]/div/calcite-switch//div/div/div")
filt_toggle.click()
print("Toggle initiated")

#Button to download csv
dwnload = driver.find_element(By.XPATH, "//*[@id='ember44']/div/div/div[1]/div/div/div[3]/hub-download-card//calcite-card/div/calcite-button")
dwnload.click()
print("Downloading csv")

sleep(180)

#Close browser window when complete
driver.close()                                

print(arcgis.__version__)