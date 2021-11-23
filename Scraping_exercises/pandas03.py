#INDIANAPOLIS
#https://databases.indystar.com/indianapolis-crime-list-of-all-criminal-homicides-in-2021/
#TUTORIAL: https://www.youtube.com/watch?v=JLDbAx6LAdo

#Import libraries
from selenium import webdriver
chrome_path = r"/Users/kellyquinn/Downloads/chromedriver"
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome(chrome_path)
driver.implicitly_wait(10)

driver.get("https://databases.indystar.com/indianapolis-crime-list-of-all-criminal-homicides-in-2021/")
driver.maximize_window()

incident_number = driver.find_elements(By.XPATH, "//*[@id='csp-data']/div/div[3]/div/div[1]/table/tbody/tr/td[1]/a")
incident_date = driver.find_elements(By.XPATH, "//*[@id='csp-data']/div/div[3]/div/div[1]/table/tbody/tr/td[2]")
incident_location = driver.find_elements(By.XPATH, "//*[@id='csp-data']/div/div[3]/div/div[1]/table/tbody/tr/td[3]")
victim_id = driver.find_elements(By.XPATH, "//*[@id='csp-data']/div/div[3]/div/div[1]/table/tbody/tr/td[4]")
victim_race = driver.find_elements(By.XPATH, "//*[@id='csp-data']/div/div[3]/div/div[1]/table/tbody/tr/td[5]")
victim_sex = driver.find_elements(By.XPATH, "//*[@id='csp-data']/div/div[3]/div/div[1]/table/tbody/tr/td[6]")
victim_age = driver.find_elements(By.XPATH, "//*[@id='csp-data']/div/div[3]/div/div[1]/table/tbody/tr/td[7]")  
incident_method = driver.find_elements(By.XPATH, "//*[@id='csp-data']/div/div[3]/div/div[1]/table/tbody/tr/td[8]")                    

#For Loop through incidents
for incidents in incident_number:
    print("Incident Number:" + incidents.text)

#For Loop through incident dates
for incidents in incident_date:
    print("Incident Date:" + incidents.text)

#For Loop through incident locations
for incidents in incident_location:
    print("Incident Location:" + incidents.text)

#For Loop through victim IDs
for victim in victim_id:
    print("Victim ID:" + victim.text)

#For Loop through victim race
for victim in victim_race:
    print("Victim Race:" + victim.text)
    
#For Loop through victim sex
for victim in victim_sex:
    print("Victim Sex:" + victim.text)

#For Loop through victim ages
for victim in victim_age:
    print("Victim Age:" + victim.text)

#For Loop through incident method
for methods in incident_method:
    print("Homicide Method:" + methods.text)

#Close browser window when complete
driver.close()