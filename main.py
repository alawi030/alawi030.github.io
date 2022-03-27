from bs4 import BeautifulSoup
import requests

with open ('index.html') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')


#scrape the whole div
for div in soup.find_all('div'):
    #scrape a specific part of the div
    
    #scrape the header of all divs
    headline= div.h2.text
    print(headline)
   
     #scrape the paragraph of all divs
    paragraph= div.p.text
    print(paragraph)
   
     #print a blank line in between
    print()