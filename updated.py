# Importing the required packages
import tkinter as tk
from tkinter import *
import requests
import geocoder
import time
import json
from datetime import datetime

# Defining the root window
root = Tk()
root.title("Weather Now")

# Defining the window size

# Defining the variables
api_key = "8a7a7bedb7f79d4e68c2405b11725a61"
global geo_position
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

    def update_weather():

        # upadte lat value
        lat = geo_position[0]
        lon = geo_position[1]
        temperature_data.config(text=str(data["current"]["temp"]) + " C")
        humidity_data.config(text=data["current"]["humidity"])
        wind_speed_data.config(text=data["current"]["wind_speed"])
        weather_desc_data.config(text=data["current"]["weather"][0]["main"].title())
        time_zone_data.config(text=data["timezone"])
        feelslike_data.config(text=data["current"]["feels_like"])
        pressure_data.config(text=data["current"]["pressure"])
        uvi_data.config(text=data["current"]["uvi"])
        sunrise_data.config(text=time.strftime('%H:%M:%S', time.gmtime(data["current"]["sunrise"])))
        sunset_data.config(text=time.strftime('%H:%M:%S', time.gmtime(data["current"]["sunset"])))
        temperature_data.after(100,update_weather)
        humidity_data.after(100,update_weather)
        wind_speed_data.after(100,update_weather)
        weather_desc_data.after(100,update_weather)
        time_zone_data.after(100,update_weather)
        feelslike_data.after(100,update_weather)
        pressure_data.after(100,update_weather)
        uvi_data.after(100,update_weather)
        sunrise_data.after(100,update_weather)
        sunset_data.after(100,update_weather)
        root.after(100,update_weather)
    
    def update_clock():
        clock.config(text=datetime.now().strftime("%H:%M:%S"))
        clock.after(100,update_clock)
    
    def update_date():
        date.config(text=datetime.now().strftime("%d/%m/%Y"))
        date.after(100,update_date)

except:
    print("Unable to Fetch Data")

# Adding logo image
logo = PhotoImage(file="weather.png")
logo_label = Label(root, image=logo)
logo_label.grid(row=0, column=0, columnspan=2)

# Adding clock label
clock = Label(root,text="Clock", font=("times", 20, "bold"), bg="white")
clock.grid(row=0, column=0, padx=10, pady=10)
update_clock()

# Adding clock data
clock_data = Label(root, font=("times", 20, "bold"), bg="white")
clock_data.grid(row=0, column=1, padx=10, pady=10)

# Adding date label
date = Label(root,text="Date", font=("times", 20, "bold"), bg="white")
date.grid(row=0, column=1, padx=10, pady=10)
update_date()

# Adding date data
date_data = Label(root, font=("times", 20, "bold"), bg="white")
date_data.grid(row=0, column=1, padx=10, pady=10)


# Adding location label
location = Label(root,text="Location" ,font=("times", 20, "bold"), bg="white")
location.grid(row=0, column=2, padx=10, pady=10)


# Adding temperature label
temperature = Label(root, text="Temperature", font=("times", 20, "bold"), bg="white")
temperature.grid(row=1, column=0, padx=10, pady=10)

# Adding temperature data label
temperature_data = Label(root, font=("times", 20, "bold"), bg="white")
temperature_data.grid(row=1, column=1, padx=10, pady=10)
update_weather()

# Adding humidity label
humidity = Label(root, text="Humidity", font=("times", 20, "bold"), bg="white")
humidity.grid(row=2, column=0, padx=10, pady=10)

# Adding humidity data label
humidity_data = Label(root, font=("times", 20, "bold"), bg="white")
humidity_data.grid(row=2, column=1, padx=10, pady=10)
update_weather()

# Adding wind speed label
wind_speed = Label(root, text="Wind Speed", font=("times", 20, "bold"), bg="white")
wind_speed.grid(row=3, column=0, padx=10, pady=10)

# Adding wind speed data label
wind_speed_data = Label(root, font=("times", 20, "bold"), bg="white")
wind_speed_data.grid(row=3, column=1, padx=10, pady=10)
update_weather()

# Adding weather description label
weather_desc = Label(root, text="Weather Description", font=("times", 20, "bold"), bg="white")
weather_desc.grid(row=4, column=0, padx=10, pady=10)

# Adding weather description data label
weather_desc_data = Label(root, font=("times", 20, "bold"), bg="white")
weather_desc_data.grid(row=4, column=1, padx=10, pady=10)
update_weather()

# Adding time zone label
time_zone = Label(root, text="Time Zone", font=("times", 20, "bold"), bg="white")
time_zone.grid(row=5, column=0, padx=10, pady=10)

# Adding time zone data label
time_zone_data = Label(root, font=("times", 20, "bold"), bg="white")
time_zone_data.grid(row=5, column=1, padx=10, pady=10)
update_weather()

# Adding feels like label
feelslike = Label(root, text="Feels Like", font=("times", 20, "bold"), bg="white")
feelslike.grid(row=6, column=0, padx=10, pady=10)

# Adding feels like data label
feelslike_data = Label(root, font=("times", 20, "bold"), bg="white")
feelslike_data.grid(row=6, column=1, padx=10, pady=10)
update_weather()

# Adding pressure label
pressure = Label(root, text="Pressure", font=("times", 20, "bold"), bg="white")
pressure.grid(row=7, column=0, padx=10, pady=10)

# Adding pressure data label
pressure_data = Label(root, font=("times", 20, "bold"), bg="white")
pressure_data.grid(row=7, column=1, padx=10, pady=10)
update_weather()

# Adding uvi label
uvi = Label(root, text="UVI", font=("times", 20, "bold"), bg="white")
uvi.grid(row=8, column=0, padx=10, pady=10)

# Adding uvi data label
uvi_data = Label(root, font=("times", 20, "bold"), bg="white")
uvi_data.grid(row=8, column=1, padx=10, pady=10)
update_weather()

# Adding sunrise label
sunrise = Label(root, text="Sunrise", font=("times", 20, "bold"), bg="white")
sunrise.grid(row=9, column=0, padx=10, pady=10)

# Adding sunrise data label
sunrise_data = Label(root, font=("times", 20, "bold"), bg="white")
sunrise_data.grid(row=9, column=1, padx=10, pady=10)
update_weather()

# Adding sunset label
sunset = Label(root, text="Sunset", font=("times", 20, "bold"), bg="white")
sunset.grid(row=10, column=0, padx=10, pady=10)

# Adding sunset data label
sunset_data = Label(root, font=("times", 20, "bold"), bg="white")
sunset_data.grid(row=10, column=1, padx=10, pady=10)
update_weather()

# Adding visibility label
visibility = Label(root, text="Visibility", font=("times", 20, "bold"), bg="white")
visibility.grid(row=11, column=0, padx=10, pady=10)

# Adding visibility data label
visibility_data = Label(root, font=("times", 20, "bold"), bg="white")
visibility_data.grid(row=11, column=1, padx=10, pady=10)
update_weather()

# Adding wind direction label
wind_direction = Label(root, text="Wind Direction", font=("times", 20, "bold"), bg="white")
wind_direction.grid(row=12, column=0, padx=10, pady=10)

# Adding wind direction data label
wind_direction_data = Label(root, font=("times", 20, "bold"), bg="white")
wind_direction_data.grid(row=12, column=1, padx=10, pady=10)
update_weather()

# Adding wind gust label
wind_gust = Label(root, text="Wind Gust", font=("times", 20, "bold"), bg="white")
wind_gust.grid(row=13, column=0, padx=10, pady=10)

# Adding wind gust data label
wind_gust_data = Label(root, font=("times", 20, "bold"), bg="white")
wind_gust_data.grid(row=13, column=1, padx=10, pady=10)
update_weather()

# Adding dew point label
dew_point = Label(root, text="Dew Point", font=("times", 20, "bold"), bg="white")
dew_point.grid(row=14, column=0, padx=10, pady=10)

# Adding dew point data label
dew_point_data = Label(root, font=("times", 20, "bold"), bg="white")
dew_point_data.grid(row=14, column=1, padx=10, pady=10)
update_weather()


root.mainloop()