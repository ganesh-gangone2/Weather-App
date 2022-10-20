from math import floor
import tkinter as tk
from tkinter import *
from turtle import update
import requests
import geocoder
import time
import json
from datetime import datetime

root = Tk()
root.title("Whats Weather Now")
root.geometry("1300x700")
root.resizable(False,False)

try:
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
    
    def update_Weather():
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
    
    def update_temperature():
        temperature_data.config(text=str(data1["current"]["temp"]) + " C")
        temperature_data.after(100,update_temperature)

    def update_humidity():
        humidity_data.config(text=str(data1["current"]["humidity"]) + " %")
        humidity_data.after(100,update_humidity)

    def update_wind_speed():
        wind_speed_data.config(text=str(data1["current"]["wind_speed"]) + " meter/sec")
        wind_speed_data.after(100,update_wind_speed)

    def update_weather_desc():
        weather_desc_data.config(text=data1["current"]["weather"][0]["main"].title())
        weather_desc_data.after(100,update_weather_desc)

    def update_time_zone():
        time_zone_data.config(text=data1["timezone"])
        time_zone_data.after(100,update_time_zone)

    def update_feelslike():
        feelslike_data.config(text=str(data1["current"]["feels_like"]) + " C")
        feelslike_data.after(100,update_feelslike)

    def update_pressure():
        pressure_data.config(text=str(data1["current"]["pressure"]) + " hPa")
        pressure_data.after(100,update_pressure)

    def update_uvi():
        uvi_data.config(text=data1["current"]["uvi"])
        uvi_data.after(100,update_uvi)

    def update_clock():
        hours=time.strftime("%I")
        minutes=time.strftime("%M")
        seconds=time.strftime("%S")
        am_or_pm=time.strftime("%p")
        time_text=hours+":"+minutes+":"+seconds+" "+am_or_pm
        digital_clock_lbl.config(text=time_text)
        digital_clock_lbl.after(100,update_clock)#after every 100 milli seconds the clock will be updated

    def update_date():
        date = datetime.now()
        text1 = f"{date:%d / %m / %Y\n%A}"
        date_time_lbl.config(text=text1)
        date_time_lbl.after(100,update_date)

except:
    print("Unable to Fetch Data")
    status_lbl = Label(root, text="Unabel to Fetch Data",font=("arial",20,"bold"))
    status_lbl.place(x=200, y=300)

get_Weather()

# Adding Logo
logo = PhotoImage(file="weather.png")
logo_label = Label(root, image=logo)
logo_label.place(x=50, y=100)

# Adding Search Box
Search_image = PhotoImage(file="search.png")
image_search_bar = Label(image=Search_image)

# Adding Search icon
Search_icon = PhotoImage(file="search_icon.png")
image_search_icon = Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040")

# Adding Time Data
digital_clock_lbl=Label(root,text="00.00.00",font=("ds-digital",20))
digital_clock_lbl.place(x=1100,y=50)
update_clock()

# Adding Date Data
date = datetime.now()
date_time_lbl = Label(root, text=f"{date:%d / %m / %Y\n%A}", font=("poppins", 15))
date_time_lbl.place(x=1100, y=90)
update_date()

# Adding Temperature Data
temperature_data = Label(text=str(floor(data1["current"]["temp"])) + " C", font=("arial",60,"bold"))
temperature_data.place(x=700,y=50)
update_temperature()

# Adding Time Zone Data 
time_zone_data = Label(text=data1["timezone"], font=("arial",20,"bold"))
time_zone_data.place(x=700,y=140)
update_time_zone()

# Adding Weather Description Data
weather_desc_data = Label(text=data1["current"]["weather"][0]["main"].title(), font=("arial",20,"bold"))
weather_desc_data.place(x=700,y=180)
update_weather_desc()

# Adding Wind Speed Label
Wind_speed_lbl = Label(root, text="WIND              :", font= ("arial",15,"bold"))
Wind_speed_lbl.place(x=700,y=300)

# Adding Wind Speed Data
wind_speed_data= Label(text= str(data1["current"]["wind_speed"]) + " meter/sec", font=("arial",15,"bold"))
wind_speed_data.place(x=900,y=300)
update_wind_speed()

# Adding Humidity Label
humidity_lbl = Label(root, text="HUMIDITY       :", font= ("poppins",15, "bold"))
humidity_lbl.place(x=700,y=340)

# Adding Humidity Data
humidity_data = Label(text=str(data1["current"]["humidity"])+ "%", font=("arial",15,"bold"))
humidity_data.place(x=900,y=340)
update_humidity()

# Adding Feels Like Label
feelslike_lbl = Label(root, text="FEELS LIKE    :", font=("arial",15,"bold"))
feelslike_lbl.place(x=700,y=380)

# Adding Feels Like Data
feelslike_data = Label(root, text=str(data1["current"]["feels_like"]) + " C",font=("arial",15,"bold"))
feelslike_data.place(x=900,y=380)
update_feelslike()

# Adding Pressure Label
pressure_lbl = Label(root, text="PRESSURE     :", font=("arial",15,"bold"))
pressure_lbl.place(x=700,y=420)

# Adding Pressure Data
pressure_data = Label(root, text=str(data1["current"]["pressure"]) + " hPa",font=("arial",15,"bold"))
pressure_data.place(x=900,y=420)
update_pressure()

# Adding UVI Label
uvi_lbl = Label(root, text="UVI                  :", font=("arial",15,"bold"))
uvi_lbl.place(x=700,y=460)

# Adding UVI Data
uvi_data = Label(root, text=data1["current"]["uvi"],font=("arial",15,"bold"))
uvi_data.place(x=900,y=460)
update_uvi()
update_Weather()
root.mainloop()
