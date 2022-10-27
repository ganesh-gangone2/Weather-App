import requests
import geocoder
g = geocoder.ip('me')
cordinates = g.latlng
global geo_position
geo_position = cordinates
lis = list(g)
lis = lis[0]
print(lis)
location = []
for i in lis:
    location.append(i)
print(location)

# [[Hyderābād, Telangana, IN]]