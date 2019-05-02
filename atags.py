import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
#commented out
#import re

url = input('Enter URL: ')

count = int(input('Enter count: '))
position = int(input('Enter position: '))

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

print('Retrieving: ' + url)

for itiration in range(count):
    url = tags[position-1].get('href')
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print('Retrieving: ' + url)

#commented out
#print(re.findall('that ([^ ]+) ', soup('h1')[0].text)[0])
