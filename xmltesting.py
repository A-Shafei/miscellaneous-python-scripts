import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)

counts = tree.findall('comments/comment/count')

for index, count in enumerate(counts):
    del counts[index]
    counts.insert(index, int(count.text))

print(sum(counts))
