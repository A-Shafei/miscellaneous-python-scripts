import urllib.request, urllib.parse, urllib.error
import json

baseurl = "http://py4e-data.dr-chuck.net/geojson?"
address = input("Enter location: ")
url = baseurl + urllib.parse.urlencode({'address': address})
data = urllib.request.urlopen(url).read().decode()

print(data)

'''
Here is the problem, the bloody thing gives me one
result for South Federal University, but SIX
results for University of Essex, with six different
place ids
'''
