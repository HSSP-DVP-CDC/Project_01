#Houston, TX
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
# Create a quickstart.py file and save in the working directory
# Ensure that the API key is saved as 'credentials.json' in the working directory

#Import selenium libraries and chrome driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

#Import Google Drive
#USERNAME: hsspdvpcdc@gmail.com
#PASSWORD: HSSP-DVP-CDC
from import drive
drive._mount('/content/gdrive')

#Import time and pandas
import time 
from time import sleep
import pandas as pd