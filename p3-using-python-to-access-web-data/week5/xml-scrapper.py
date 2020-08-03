# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
# http://py4e-data.dr-chuck.net/comments_857073.xml

import urllib.request
import xml.etree.ElementTree as ET

url = input("Please enter xml URL: ")
try:
    response = urllib.request.urlopen(url)
except:
    print("Invalid URL provided.")
    quit()

tree = ET.fromstring(response.read())
counts = tree.findall(".//count")

value = sum([int(count.text) for count in counts])
# altrnate of above line
#for count in counts:
#    value = value + int(count.text)

print(value)