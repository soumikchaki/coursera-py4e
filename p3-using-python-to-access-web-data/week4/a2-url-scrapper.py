# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat
# the process a number of times and report the last name you find.
#  http://py4e-data.dr-chuck.net/known_by_Grace.html

import urllib.request, urllib.error
from bs4 import BeautifulSoup

url = input("Please enter an URL: ")
tries = input("Please enter number of tries: ") #7
pos = input("Please enter position: ") #18
name = ""

for i in range(int(tries)):
    try:
        response = urllib.request.urlopen(url)
    except:
        print("Invalid URL provided.")
        quit()

    bs = BeautifulSoup(response.read(), "html.parser")
    tag = bs("a")[int(pos)-1]
    name = tag.get_text()
    url = tag.get("href")

print(name)



