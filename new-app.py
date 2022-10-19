import tkinter as tk
from tkinter import *
from turtle import update
import requests
import geocoder
import time
import json
from datetime import datetime

root = Tk()
root.title("Weather Now")


try:
    def getWeather():
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
    
    def update_Weather():



        temperature_data.config(text=str(data1["current"]["temp"]) + " C")
        temperature_data.after(100,update_Weather)

        humidity_data.config(text=data1["current"]["humidity"])
        humidity_data.after(100,update_Weather)

        wind_speed_data.config(text=data1["current"]["wind_speed"])
        wind_speed_data.after(100,update_Weather)

        weather_desc_data.config(text=data1["current"]["weather"][0]["main"].title())
        weather_desc_data.after(100,update_Weather)

        time_zone_data.config(text=data1["timezone"])
        time_zone_data.after(100,update_Weather)

        feelslike_data.config(text=data1["current"]["feels_like"])
        feelslike_data.after(100,update_Weather)

        pressure_data.config(text=data1["current"]["pressure"])
        pressure_data.after(100,update_Weather)

        uvi_data.config(text=data1["current"]["uvi"])
        uvi_data.after(100,update_Weather)

        hours=time.strftime("%I")
        minutes=time.strftime("%M")
        seconds=time.strftime("%S")
        am_or_pm=time.strftime("%p")
        time_text=hours+":"+minutes+":"+seconds+" "+am_or_pm
        digital_clock_lbl.config(text=time_text)
        digital_clock_lbl.after(100,update_Weather)

        date = datetime.now()
        text1 = f"{date:%d / %m / %Y\n%A}"
        date_time_lbl.config(text=text1)
        date_time_lbl.after(100,update_Weather)

except:
    print("Unable to Fetch Data")

getWeather()

# Adding Logo
logo = PhotoImage(file="weather.png")
logo_label = Label(root, image=logo)


# Adding Search Box
Search_image = PhotoImage(file="search.png")
image_search_bar = Label(image=Search_image)

# Adding Search icon
Search_icon = PhotoImage(file="search_icon.png")
image_search_icon = Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040")

# Adding Time Data
digital_clock_lbl=Label(root,text="00.00.00",font=("ds-digital",20),fg="#404040")
digital_clock_lbl.place(x=100,y=50)

# Adding Date Data
date = datetime.now()
date_time_lbl = Label(root, text=f"{date:%d / %m / %Y\n%A}", font=("poppins", 10))

# Adding Temperature Data
temperature_data = Label(text=str(data1["current"]["temp"]) + " C", font=("arial",60,"bold"))

# Adding Time Zone Label 
time_zone_data = Label(text=data1["timezone"], font=("arial",20,"bold"))

# Adding Weather Description Data
weather_desc_data = Label(text=data1["current"]["weather"][0]["main"].title(), font=("arial",20,"bold"))

# Adding Wind Speed Label
Wind_speed_lbl = Label(root, text="WIND", font= ("arial",15, "bold"),fg = "#404040")

# Adding Wind Speed Data
wind_speed_data= Label(text= data1["current"]["wind_speed"], font=("arial",20,"bold"))

# Adding Humidity Label
humidity_lbl = Label(root, text="HUMIDITY", font= ("poppins",15, "bold"),fg = "#404040")

# Adding Humidity Data
humidity_data = Label(text=data1["current"]["humidity"], font=("arial",20,"bold"))

# Adding Feels Like Label
feelslike_lbl = Label(root, text="FELLS LIKE", font=("arial",15,"bold"),fg="#404040")

# Adding Feels Like Data
feelslike_data = Label(root, text=data1["current"]["feels_like"],font=("arial",20,"bold"))

# Adding Pressure Label
pressure_lbl = Label(root, text="PRESSURE", font=("arial",15,"bold"),fg="#404040")

# Adding Pressure Data
pressure_data = Label(root, text=data1["current"]["pressure"],font=("arial",20,"bold"))

# Adding UVI Label
uvi_lbl = Label(root, text="UVI", font=("arial",15,"bold"),fg="#404040")

# Adding UVI Data
uvi_data = Label(root, text=data1["current"]["uvi"],font=("arial",20,"bold"))

update_Weather()

root.mainloop()
