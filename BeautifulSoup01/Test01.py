#Test Run
import requests
from bs4 import BeautifulSoup

#Create a variable to store the result of accessing the page
result = requests.get("https://www.google.com/")

#Ask the program to return a code if the page is accessible. "200" is good.
print(result.status_code)
print (result.headers)

#extract the content
source = result.content 
print(source)

#create Soup Object
soup = BeautifulSoup(source, 'lxml')

#create a Links variable
links = soup.find_all("a")
print(links)
print("\n")

#Loop through the links
for link in links:
    if "About" in link.text:
        print(link)
        #Give me the content of that attribute "href" within the 'a' tag
        print(link.attrs['href'])