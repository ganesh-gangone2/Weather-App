import tkinter as tk
from tkinter import *
import requests
import geocoder
import time
import json
from datetime import datetime

root = Tk()
root.title("Weather Now")

api_key = "8a7a7bedb7f79d4e68c2405b11725a61"

try:
    def getWeather():
        g = geocoder.ip('me')
        cordinates = g.latlng
        global geo_position
        geo_position = cordinates
        lat = cordinates[0]
        lon = cordinates[1]
        url1 = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
        response = requests.get(url1)
        api_data = json.loads(response.text)
        global data
        data = api_data

except:
    print("Unable to Fetch Data")

logo = PhotoImage(file="weather.png")
logo_label = Label(root, image=logo)

root.mainloop()