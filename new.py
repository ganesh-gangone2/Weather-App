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
root.resizable(True,True)

# Handling No Internet Connection Error
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

    def update_weather_icon():
        weather_icon_data.config(text=data1["current"]["weather"][0]["icon"])
        weather_icon_data.after(100,update_weather_icon)
    
    def update_sunrise():
        sunrise_data.config(text=datetime.fromtimestamp(data1["current"]["sunrise"]).strftime("%H:%M:%S"))
        sunrise_data.after(100,update_sunrise)
    
    def update_sunset():
        sunset_data.config(text=datetime.fromtimestamp(data1["current"]["sunset"]).strftime("%H:%M:%S"))
        sunset_data.after(100,update_sunset)
    
    def update_feels_like():
        feels_like_data.config(text=str(data1["current"]["feels_like"]) + " C")
        feels_like_data.after(100,update_feels_like)
    
    def update_dew_point():
        dew_point_data.config(text=str(data1["current"]["dew_point"]) + " C")
        dew_point_data.after(100,update_dew_point)
    
    def update_uvi():
        uvi_data.config(text=str(data1["current"]["uvi"]))
        uvi_data.after(100,update_uvi)
    
    def update_clouds():
        clouds_data.config(text=str(data1["current"]["clouds"]) + " %")
        clouds_data.after(100,update_clouds)
    
    def update_visibility():
        visibility_data.config(text=str(data1["current"]["visibility"]) + " meter")
        visibility_data.after(100,update_visibility)
    
    def update_pressure():
        pressure_data.config(text=str(data1["current"]["pressure"]) + " hPa")
        pressure_data.after(100,update_pressure)
    
    def update_dew_point():
        dew_point_data.config(text=str(data1["current"]["dew_point"]) + " C")
        dew_point_data.after(100,update_dew_point)

    def update_hourly():
        hourly_data.config(text=str(data1["hourly"][0]["temp"]) + " C")
        hourly_data.after(100,update_hourly)

    def update_daily():
        daily_data.config(text=str(data1["daily"][0]["temp"]["day"]) + " C")
        daily_data.after(100,update_daily)
    
    def update_minutely():
        minutely_data.config(text=str(data1["minutely"][0]["precipitation"]) + " mm")
        minutely_data.after(100,update_minutely)
    
    def update_alerts():
        alerts_data.config(text=data1["alerts"][0]["event"])
        alerts_data.after(100,update_alerts)
    
    def update_timezone():
        timezone_data.config(text=data1["timezone"])
        timezone_data.after(100,update_timezone)
    
    def update_lat():
        lat_data.config(text=str(geo_position[0]))
        lat_data.after(100,update_lat)
    
    def update_lon():
        lon_data.config(text=str(geo_position[1]))
        lon_data.after(100,update_lon)
    
    def update_current_time():
        current_time_data.config(text=datetime.now().strftime("%H:%M:%S"))
        current_time_data.after(100,update_current_time)
    
    def update_current_date():
        current_date_data.config(text=datetime.now().strftime("%d/%m/%Y"))
        current_date_data.after(100,update_current_date)
    
    def update_current_day():
        current_day_data.config(text=datetime.now().strftime("%A"))
        current_day_data.after(100,update_current_day)
    
    def update_current_month():
        current_month_data.config(text=datetime.now().strftime("%B"))
        current_month_data.after(100,update_current_month)
    
    def update_current_year():
        current_year_data.config(text=datetime.now().strftime("%Y"))
        current_year_data.after(100,update_current_year)
    
    def update_current_weekday():
        current_weekday_data.config(text=datetime.now().strftime("%w"))
        current_weekday_data.after(100,update_current_weekday)
    
    def update_current_week():
        current_week_data.config(text=datetime.now().strftime("%W"))
        current_week_data.after(100,update_current_week)
    
    def update_current_quarter():
        current_quarter_data.config(text=datetime.now().strftime("%q"))
        current_quarter_data.after(100,update_current_quarter)
    
    def update_current_day_of_year():
        current_day_of_year_data.config(text=datetime.now().strftime("%j"))
        current_day_of_year_data.after(100,update_current_day_of_year)
    
    def update_current_day_of_month():
        current_day_of_month_data.config(text=datetime.now().strftime("%d"))
        current_day_of_month_data.after(100,update_current_day_of_month)
    
    def update_current_day_of_week():
        current_day_of_week_data.config(text=datetime.now().strftime("%A"))
        current_day_of_week_data.after(100,update_current_day_of_week)
    
    def update_current_hour():
        current_hour_data.config(text=datetime.now().strftime("%H"))
        current_hour_data.after(100,update_current_hour)
    
    def update_current_minute():
        current_minute_data.config(text=datetime.now().strftime("%M"))
        current_minute_data.after(100,update_current_minute)
    
    def update_current_second():
        current_second_data.config(text=datetime.now().strftime("%S"))
        current_second_data.after(100,update_current_second)
    
except:
    print("Error")
    root.destroy()
    exit()


# Creating Labels
# Temperature
temperature_label = Label(root, text="Temperature", font=("Arial", 15, "bold"))
temperature_label.place(x=10, y=10)

temperature_data = Label(root, text="0 C", font=("Arial", 15))
temperature_data.place(x=10, y=40)

# Humidity
humidity_label = Label(root, text="Humidity", font=("Arial", 15, "bold"))
humidity_label.place(x=10, y=70)

humidity_data = Label(root, text="0 %", font=("Arial", 15))
humidity_data.place(x=10, y=100)

# Wind Speed
wind_speed_label = Label(root, text="Wind Speed", font=("Arial", 15, "bold"))
wind_speed_label.place(x=10, y=130)

wind_speed_data = Label(root, text="0 m/s", font=("Arial", 15))
wind_speed_data.place(x=10, y=160)

# Weather Desc
weather_desc_label = Label(root, text="Wind Desc", font=("Arial", 15, "bold"))
weather_desc_label.place(x=10, y=190)

weather_desc_data = Label(root, text="N/A", font=("Arial", 15))
weather_desc_data.place(x=10, y=220)

# Weather icon data
weather_icon_label = Label(root, text="Weather Icon", font=("Arial", 15, "bold"))
weather_icon_label.place(x=10, y=250)

weather_icon_data = Label(root, text="N/A", font=("Arial", 15))
weather_icon_data.place(x=10, y=280)

# Sunrise data
sunrise_label = Label(root, text="Sunrise", font=("Arial", 15, "bold"))
sunrise_label.place(x=10, y=310)

sunrise_data = Label(root, text="N/A", font=("Arial", 15))
sunrise_data.place(x=10, y=340)

# Sunset data
sunset_label = Label(root, text="Sunset", font=("Arial", 15, "bold"))
sunset_label.place(x=10, y=370)

sunset_data = Label(root, text="N/A", font=("Arial", 15))
sunset_data.place(x=10, y=400)

# feels like data
feels_like_label = Label(root, text="Feels Like", font=("Arial", 15, "bold"))
feels_like_label.place(x=10, y=430)

feels_like_data = Label(root, text="N/A", font=("Arial", 15))
feels_like_data.place(x=10, y=460)

# dew point data
dew_point_label = Label(root, text="Dew Point", font=("Arial", 15, "bold"))
dew_point_label.place(x=10, y=490)

dew_point_data = Label(root, text="N/A", font=("Arial", 15))
dew_point_data.place(x=10, y=520)

# uvi data
uvi_label = Label(root, text="UVI", font=("Arial", 15, "bold"))
uvi_label.place(x=10, y=550)

uvi_data = Label(root, text="N/A", font=("Arial", 15))
uvi_data.place(x=10, y=580)

# Clouds data
clouds_label = Label(root, text="Clouds", font=("Arial", 15, "bold"))
clouds_label.place(x=10, y=610)

clouds_data = Label(root, text="N/A", font=("Arial", 15))
clouds_data.place(x=10, y=640)

# Visibility data
visibility_label = Label(root, text="Visibility", font=("Arial", 15, "bold"))
visibility_label.place(x=10, y=670)

visibility_data = Label(root, text="N/A", font=("Arial", 15))
visibility_data.place(x=10, y=700)

# Pressure data
pressure_label = Label(root, text="Pressure", font=("Arial", 15, "bold"))
pressure_label.place(x=10, y=730)

pressure_data = Label(root, text="N/A", font=("Arial", 15))
pressure_data.place(x=10, y=760)

# Hourly data
hourly_label = Label(root, text="Hourly", font=("Arial", 15, "bold"))
hourly_label.place(x=10, y=790)

hourly_data = Label(root, text="N/A", font=("Arial", 15))
hourly_data.place(x=10, y=820)

# Daily data
daily_label = Label(root, text="Daily", font=("Arial", 15, "bold"))
daily_label.place(x=10, y=850)

daily_data = Label(root, text="N/A", font=("Arial", 15))
daily_data.place(x=10, y=880)

# minutely data
minutely_label = Label(root, text="Minutely", font=("Arial", 15, "bold"))
minutely_label.place(x=10, y=910)

minutely_data = Label(root, text="N/A", font=("Arial", 15))
minutely_data.place(x=10, y=940)

# Alerts data
alerts_label = Label(root, text="Alerts", font=("Arial", 15, "bold"))
alerts_label.place(x=10, y=970)

alerts_data = Label(root, text="N/A", font=("Arial", 15))
alerts_data.place(x=10, y=1000)

# Timezone data
timezone_label = Label(root, text="Timezone", font=("Arial", 15, "bold"))
timezone_label.place(x=10, y=1030)

timezone_data = Label(root, text="N/A", font=("Arial", 15))
timezone_data.place(x=10, y=1060)

# lat data
lat_label = Label(root, text="Lat", font=("Arial", 15, "bold"))
lat_label.place(x=10, y=1090)

lat_data = Label(root, text="N/A", font=("Arial", 15))
lat_data.place(x=10, y=1120)

# lon data
lon_label = Label(root, text="Lon", font=("Arial", 15, "bold"))
lon_label.place(x=10, y=1150)

lon_data = Label(root, text="N/A", font=("Arial", 15))
lon_data.place(x=10, y=1180)

# current time data
current_time_label = Label(root, text="Current Time", font=("Arial", 15, "bold"))
current_time_label.place(x=10, y=1210)

current_time_data = Label(root, text="N/A", font=("Arial", 15))
current_time_data.place(x=10, y=1240)

# current date data
current_date_label = Label(root, text="Current Date", font=("Arial", 15, "bold"))
current_date_label.place(x=10, y=1270)

current_date_data = Label(root, text="N/A", font=("Arial", 15))
current_date_data.place(x=10, y=1300)

# current day data
current_day_label = Label(root, text="Current Day", font=("Arial", 15, "bold"))
current_day_label.place(x=10, y=1330)

current_day_data = Label(root, text="N/A", font=("Arial", 15))
current_day_data.place(x=10, y=1360)

# current month data
current_month_label = Label(root, text="Current Month", font=("Arial", 15, "bold"))
current_month_label.place(x=10, y=1390)

current_month_data = Label(root, text="N/A", font=("Arial", 15))
current_month_data.place(x=10, y=1420)

# current year data
current_year_label = Label(root, text="Current Year", font=("Arial", 15, "bold"))
current_year_label.place(x=10, y=1450)

current_year_data = Label(root, text="N/A", font=("Arial", 15))
current_year_data.place(x=10, y=1480)

# current week day data
current_week_day_label = Label(root, text="Current Week Day", font=("Arial", 15, "bold"))
current_week_day_label.place(x=10, y=1510)

current_weekday_data = Label(root, text="N/A", font=("Arial", 15))
current_weekday_data.place(x=10, y=1540)

# current week data
current_week_label = Label(root, text="Current Week", font=("Arial", 15, "bold"))
current_week_label.place(x=10, y=1570)

current_week_data = Label(root, text="N/A", font=("Arial", 15))
current_week_data.place(x=10, y=1600)

# current quarter data
current_quarter_label = Label(root, text="Current Quarter", font=("Arial", 15, "bold"))
current_quarter_label.place(x=10, y=1630)

current_quarter_data = Label(root, text="N/A", font=("Arial", 15))
current_quarter_data.place(x=10, y=1660)

# current day of year data
current_day_of_year_label = Label(root, text="Current Day of Year", font=("Arial", 15, "bold"))
current_day_of_year_label.place(x=10, y=1690)

current_day_of_year_data = Label(root, text="N/A", font=("Arial", 15))
current_day_of_year_data.place(x=10, y=1720)

# current day of month data
current_day_of_month_label = Label(root, text="Current Day of Month", font=("Arial", 15, "bold"))
current_day_of_month_label.place(x=10, y=1750)

current_day_of_month_data = Label(root, text="N/A", font=("Arial", 15))
current_day_of_month_data.place(x=10, y=1780)

# current day of week data
current_day_of_week_label = Label(root, text="Current Day of Week", font=("Arial", 15, "bold"))
current_day_of_week_label.place(x=10, y=1810)

current_day_of_week_data = Label(root, text="N/A", font=("Arial", 15))
current_day_of_week_data.place(x=10, y=1840)

# current hour data
current_hour_label = Label(root, text="Current Hour", font=("Arial", 15, "bold"))
current_hour_label.place(x=10, y=1870)

current_hour_data = Label(root, text="N/A", font=("Arial", 15))
current_hour_data.place(x=10, y=1900)

# current minute data
current_minute_label = Label(root, text="Current Minute", font=("Arial", 15, "bold"))
current_minute_label.place(x=10, y=1930)

current_minute_data = Label(root, text="N/A", font=("Arial", 15))
current_minute_data.place(x=10, y=1960)

# current second data
current_second_label = Label(root, text="Current Second", font=("Arial", 15, "bold"))
current_second_label.place(x=10, y=1990)

current_second_data = Label(root, text="N/A", font=("Arial", 15))
current_second_data.place(x=10, y=2020)

root.mainloop()