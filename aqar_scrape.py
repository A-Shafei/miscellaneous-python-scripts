from urllib.request import urlopen as opener

that_url = "https://egypt.aqarmap.com"

opened = opener(that_url)

print(dict(opened.info()))
