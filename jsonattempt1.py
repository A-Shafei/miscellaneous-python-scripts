import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
data = urllib.request.urlopen(url).read().decode()
info = json.loads(data)
comments = info["comments"]

for index, comment in enumerate(comments):
    del comments[index]
    comments.insert(index, int(comment["count"]))

print(sum(comments))
