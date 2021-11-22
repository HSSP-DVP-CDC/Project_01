#THIS IS NOT CURRENTLY WORKING CODE
from selenium import webdriver
chrome_path = r"/Users/kellyquinn/Downloads/chromedriver"
import pandas as pd
driver = webdriver.Chrome(chrome_path)
driver.implicitly_wait(30)

driver.get("https://databases.indystar.com/indianapolis-crime-list-of-all-criminal-homicides-in-2021/")
df = pd.read_html(driver.find_element_by_id("IndyStar").get_attribute('outerHTML'))[0]

print(df)
