import requests
from bs4 import BeautifulSoup

#Create a variable to store the result of accessing the page
result = requests.get("https://www.whitehouse.gov/briefings-statements")

#Ask the program to return a code if the page is accessible. "200" is good.
print(result.status_code)
#print (result.headers)

#extract the content
source = result.content 
#print(source)

#create Soup Object
soup = BeautifulSoup(source, 'lxml')

#Create a list
urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')

    if a_tag is not None and 'href' in a_tag.attrs:
        urls.append(a_tag.attrs['href'])

#print list
print (urls)
