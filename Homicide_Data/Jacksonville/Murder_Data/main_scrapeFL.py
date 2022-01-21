#Jacksonville, Florida
#Murder Data

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
prefs = {"download.default_directory":"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Jacksonville/Murder_Data"}
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
df = pd.read_csv("Homicide_Data/Jacksonville/Murder_Data/Exported Data.csv")
print(df)

print("Program complete")