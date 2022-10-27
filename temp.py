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


# icon id
icon_id = data1["current"]["weather"][0]["icon"]
# icon url
icon_url = "http://openweathermap.org/img/wn/" + icon_id + ".png"
# Downloading icon
urllib.request.urlretrieve(icon_url, "icon.png")
# Opening icon
icon = Image.open("icon.png")
# Resizing icon
icon = icon.resize((100, 100), Image.ANTIALIAS)
# Saving icon
icon.save("icon.png")
# Opening icon
icon = Label(window,Image.open("icon.png"))
# Displaying icon
icon_label = Label(canvas, image=icon)
icon_label.place(x=10, y=15)