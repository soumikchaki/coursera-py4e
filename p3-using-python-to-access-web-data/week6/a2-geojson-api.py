# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
# University of Hawaii

import urllib.request, urllib.parse
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

location = input("Please enter a location: ")
params = dict()
params["address"] = location
if api_key is not False: params["key"] = api_key
json_url = serviceurl + urllib.parse.urlencode(params)
# print(json_url)

handler = urllib.request.urlopen(json_url)
data = json.loads(handler.read().decode())
place_id = data["results"][0]["place_id"]

print(place_id)