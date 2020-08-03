# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
# http://py4e-data.dr-chuck.net/comments_857074.json

import urllib.request
import json

url = input("Please enter JSON URL: ")
try:
    response = urllib.request.urlopen(url)
except:
    print("Invalid URL provided.")
    quit()

load = json.loads(response.read())
comments = load["comments"]

value = 0

for item in comments:
    value = value + int(item["count"])

print(value)