# Trying to scrape the hell out of Aqarmap.com is a good way to get used to it's
# html structure in anticipation of automating its testing
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

request_clint = urllib.request.urlopen('https://egypt.aqarmap.com/en/for-sale/apartment/suez/')
page_html = request_clint.read()
request_clint.close()

page_soup = BeautifulSoup(page_html, 'html.parser')

searchResultsContainer = page_soup.body.find_all('div', recursive=False)[4]

stepping_down1 = searchResultsContainer.find_all('div', recursive=False)[1]
stepping_down2 = stepping_down1.find_all('section', recursive=False)[0]
sectionBody = stepping_down2.find_all(class_='sectionBody')[0]

search_cards = sectionBody.ul.find_all('li')

print(len(search_cards))
