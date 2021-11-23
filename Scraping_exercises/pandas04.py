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

#Homcide Results
homicide_results =[]

for i in range(len(incident_number)):
    temporary_data = {"Incident Number" : incident_number[i].text,
                      "Incident Date" : incident_date[i].text,
                      "Incident Location" : incident_location[i].text,
                      "Victim ID" : victim_id[i].text,
                      "Victim Race" : victim_race[i].text,
                      "Victim Sex" : victim_sex[i].text,
                      "Victim Age" : victim_age[i].text,
                      "Incident Method" : incident_method[i].text
                      }
    homicide_results.append(temporary_data)

df = pd.DataFrame(homicide_results)
print(df)

#Close browser window when complete
driver.close()