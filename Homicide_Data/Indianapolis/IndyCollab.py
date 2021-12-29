#Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from bs4 import BeautifulSoup

#Set Chrome Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#Set Chrome Driver 
chrome_path = r"/Users/kellyquinn/Desktop/ORISE/HSSP_Code/chromedriver"
driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.implicitly_wait(10)

html = driver.page_source
soup = BeautifulSoup(html)

all_tables = soup.findAll("table")
# murders_table = all_tables[0]

table_rows = [[td.text for td in row.find_all("td")] for row in all_tables.find_all("tr")[1:]]
table_headers = [th.text for th in all_tables.find_all("th")]

import pandas
df = pandas.DataFrame(table_rows, columns=table_headers)

print(df)