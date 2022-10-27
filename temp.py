import requests
import geocoder
g = geocoder.ip('me')
cordinates = g.latlng
global geo_position
geo_position = cordinates
lis = list(g)
lis = lis[0]


# [[Hyderābād, Telangana, IN]]
# Importing required libraries
from pathlib import Path
from math import floor
import tkinter as tk
from tkinter import *
from turtle import update
import requests
import urllib
import geocoder
import time
import json
from datetime import datetime

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Defining root window
window = Tk()

# Setting window size
window.geometry("1035x665")
window.configure(bg = "#FFFFFF")

# Defining Canvas
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 665,
    width = 1035,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# Funnction for API Call to collect weather information
def get_Weather():
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
        loc = list(g)
        global location
        location = loc

get_Weather()
# icon id
icon_id = data1["current"]["weather"][0]["icon"]
# icon url
icon_url = "http://openweathermap.org/img/wn/" + icon_id + ".png"

# Downloading icon image
urllib.request.urlretrieve(icon_url, "icon.png")
# Defining icon image
icon_img = PhotoImage(file = "icon.png")

# resizing icon

# Defining icon
# Defining icon
icon = canvas.create_image(
    515.0,
    332.5,
    image = icon_img
)

# placing icon
canvas.place(x = 0, y = 0)



window.resizable(False, False)
window.mainloop()