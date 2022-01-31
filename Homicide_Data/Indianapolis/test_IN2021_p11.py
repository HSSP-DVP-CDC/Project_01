#INDIANAPOLIS
#https://databases.indystar.com/indianapolis-crime-list-of-all-criminal-homicides-in-2021/
#TUTORIAL: https://www.youtube.com/watch?v=JLDbAx6LAdo

#Scapes into a MASTER FOLDER
# 2021 PAGE 11

#Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import pandas as pd

#Set Chrome Options
options = Options()
options.add_argument('--headless')
prefs = {"download.default_directory":"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Indianapolis/"}
options.add_experimental_option('prefs', prefs)

#Set Chrome Driver 
chrome_path = r"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/chromedriver"
driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.implicitly_wait(10)

#Fetch webpage data
driver.get("https://databases.indystar.com/indianapolis-crime-list-of-all-criminal-homicides-in-2021/page/11/")

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

#Close browser window when complete
driver.close()
print("Driver closed")

#Create a dataframe using Pandas
df = pd.DataFrame(homicide_results)
print(df)

#Export data to csv
df.to_csv('/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Indianapolis/indianapolis_homicide_data.csv', mode = 'a', index = False, header = 'False')

# Read the csv into the console
df = pd.read_csv("/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Indianapolis/indianapolis_homicide_data.csv")
print(df)

# Sort the data
# sorted_df = df.sort_values(by=["Incident Number"], ascending=False)
# print(sorted_df)

#Create new dataframe
# sorted_df.to_csv("/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Indianapolis/indianapolis_homicide_sorted.csv", index=False)

# df = pd.read_csv("/Users/kellyquinn/Desktop/ORISE/HSSP_Code/Project_01/Homicide_Data/Indianapolis/indianapolis_homicide_sorted.csv")
# print(df)

print("Program complete")
