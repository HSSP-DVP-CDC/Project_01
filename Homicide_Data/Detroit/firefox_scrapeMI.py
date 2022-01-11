# Detroit, Michigan
# Firefox

#NOT WORKING CODE AT THIS TIME!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#pip install
#pip install webdriver-manager

# Import Selenium libraries
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

#Import libraries
import time 
from time import sleep
import pandas as pd
import arcgis 
from arcgis.gis import GIS
import os


#Set FireFox options
fireFoxOptions = Options()  
fireFoxOptions.add_argument("--headless") 
fireFoxOptions.add_argument("--window-size=1920,1080")
fireFoxOptions.add_argument('--start-maximized')
fireFoxOptions.add_argument('--disable-gpu')
fireFoxOptions.add_argument('--no-sandbox')
prefs = {"download.default_directory":"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Detroit"}
fireFoxOptions.add_argument(prefs)
# fireFoxOptions.add_argument('excludeSwitches', ['enable-logging'])

# Set driver
path_executable = os.path.abs(r'Users/kellyquinn/.local/bin/geckodriver')
driver = webdriver.Firefox(executable_path = path_executable)
                        
driver.implicitly_wait(10)

#Fetch webpage data (already filtered by 'Homicide/Non-Negligent Murder')
driver.get("https://data.detroitmi.gov/datasets/rms-crime-incidents/explore?filters=eyJjaGFyZ2VfZGVzY3JpcHRpb24iOlsiTVVSREVSIC8gTk9OLU5FR0xJR0VOVCBNQU5TTEFVR0hURVIgKFZPTFVOVEFSWSkiLCJNVVJERVIgLyBOT04tTkVHTElHRU5UIE1BTlNMQVVHSFRFUiAoVk9MVU5UQVJZKSAgICAgICAgICAgICAiXSwieWVhciI6WzIwMjAuOTcsMjAyMV19&location=42.348386%2C-83.007003%2C10.62&showTable=true")
wait = WebDriverWait(driver, 60)

driver.close()
print("Test complete")