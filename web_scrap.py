import requests
from bs4 import BeautifulSoup
url="https://www.geeksforgeeks.org/binary-search/?ref=leftbar-rightbar"

# Getting the HTMl
r=requests.get(url)
htmlContent= r.content


#parsing the html

soup=BeautifulSoup(htmlContent,'html.parser')


#HTMl tree traversal

#Title of Page
title=soup.title

#Get all the paragraphs of web page
paras=soup.find_all('p')

#Get all the anchor tags from the page

anchors=soup.find_all('a')

#Get all links on the page:
all_links=set()
for link in anchors:
    if(link.get('href') !='#'):
        linkText = "https://www.geeksforgeeks.org/" +link.get('href')
         all_links.add(link)
         print(linkText)


#Get classes of any Element in the htmll page

print(soup.find('p')['class'])


#Get the text from the tags

print(soup.find('p').get_text())
print(soup.get_text())








