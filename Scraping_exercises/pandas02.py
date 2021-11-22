from selenium import webdriver
chrome_path = r"/Users/kellyquinn/Downloads/chromedriver"
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome(chrome_path)
driver.implicitly_wait(30)

driver.get("https://databases.indystar.com/indianapolis-crime-list-of-all-criminal-homicides-in-2021/")
driver.maximize_window()

incident_number01 = driver.find_element(By.XPATH, "//*[@id='csp-data']/div/div[3]/div/div[1]/table/tbody/tr[1]/td[1]/a").text
incident_number02 = driver.find_element(By.XPATH, "//*[@id='csp-data']/div/div[3]/div/div[1]/table/tbody/tr[2]/td[1]/a").text

#for incidents in incident_number:
    # print(incidents)

print(incident_number01)
print(incident_number02)
