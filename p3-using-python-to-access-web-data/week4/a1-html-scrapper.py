# Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# Actual data: http://py4e-data.dr-chuck.net/comments_857071.html (Sum ends with 53)

import urllib.request, urllib.error
import re

url = input("Please enter an URL: ")
try:
    response = urllib.request.urlopen(url)
except:
    print("Invalid URL provided.")
    quit()

html = response.read().decode()
values = re.findall("<span class=\"comments\">([0-9]+)<", html)
result = sum([int(item) for item in values])

print(result)
