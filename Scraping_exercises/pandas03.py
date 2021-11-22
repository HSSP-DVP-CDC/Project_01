#INDIANAPOLIS
#https://databases.indystar.com/indianapolis-crime-list-of-all-criminal-homicides-in-2021/
#TUTORIAL: https://www.youtube.com/watch?v=JLDbAx6LAdo

#Import libraries
from selenium import webdriver
chrome_path = r"/Users/kellyquinn/Downloads/chromedriver"
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome(chrome_path)
driver.implicitly_wait(30)

driver.get("https://databases.indystar.com/indianapolis-crime-list-of-all-criminal-homicides-in-2021/")
driver.maximize_window()

incident_number = driver.find_elements(By.XPATH, "//*[@id='csp-data']/div/div[3]/div/div[1]/table/tbody/tr/td[1]/a")
incident_date = driver.find_elements(By.XPATH, "//*[@id='csp-data']/div/div[3]/div/div[1]/table/tbody/tr/td[2]")

#For Loop through incidents
for incidents in incident_number:
    print(incidents.text)

#For Loop through incident dates
for incidents in incident_date:
    print(incidents.text)