import requests
import urllib
import geocoder
import json
g = geocoder.ip('me')
cordinates = g.latlng
global geo_position
geo_position = cordinates
api_key = "8a7a7bedb7f79d4e68c2405b11725a61"
lat = cordinates[0]
lon = cordinates[1]
url1 = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
response = requests.get(url1)
data = json.loads(response.text)
global data1
data1 = data
print(data1)