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
window.title("Weather App")
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
canvas.place(x = 0, y = 0)

try:
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

    # Function to update the digital clock
    def update_clock():
            hours=time.strftime("%I")
            minutes=time.strftime("%M")
            am_or_pm=time.strftime("%p")
            time_text=hours+":"+minutes+" "+am_or_pm
            digital_clock_lbl.config(text=time_text)
            digital_clock_lbl.after(100,update_clock)#after every 100 milli seconds the clock will be updated

    # Function to update the weather description
    def update_weather_desc():
        weather_desc_data.config(text=data1["current"]["weather"][0]["main"].title())
        weather_desc_data.after(100,update_weather_desc)

    # Function to update the date
    def update_date():
        date = datetime.now()
        text1 = f"{date:%d / %m / %Y\n%A}"
        date_time_lbl.config(text=text1)
        date_time_lbl.after(100,update_date)

    # Function to update the wind speed
    def update_wind_speed():
        wind_speed_data.config(text=str(data1["current"]["wind_speed"]) + " meter/sec")
        wind_speed_data.after(100,update_wind_speed)

    # Function to update the humidity
    def update_humidity():
        humidity_data.config(text=str(data1["current"]["humidity"]) + " %")
        humidity_data.after(100,update_humidity)

    # Function to update the Pressure
    def update_pressure():
        pressure_data.config(text=str(data1["current"]["pressure"]) + " hPa")
        pressure_data.after(100,update_pressure)

    # Function to update uvi
    def update_uvi():
        uvi_data.config(text=data1["current"]["uvi"])
        uvi_data.after(100,update_uvi)

    # Function to update the dew point
    def update_dewpoint():
        dew_point_data.config(text=str(data1["current"]["dew_point"]) + " C")
        dew_point_data.after(100,update_dewpoint)

    # Function to update visibility
    def update_visibility():
        visibility_data.config(text=str(data1["current"]["visibility"]) + " meter")
        visibility_data.after(100,update_visibility)

    # Function to convert timestamp to time
    def convert_time(timestamp):
        return datetime.fromtimestamp(timestamp).strftime("%I:%M %p")

    def convert_day(timestamp):
        return datetime.fromtimestamp(timestamp).strftime("%A")
    # Function to update the temperature
    def update_temperature():
        temperature_data.config(text=str(floor(data1["current"]["temp"])) + " ᴼ C")
        temperature_data.after(100,update_temperature)

    # Function to update the hourly forecast
    def update_hourly_forecast():
        # Updating temperature
        hour_1_temp.config(text=str(floor(data1["hourly"][0]["temp"])) + " ᴼ C")
        hour_1_temp.after(3600000,update_hourly_forecast)
        hour_2_temp.config(text=str(floor(data1["hourly"][1]["temp"])) + " ᴼ C")
        hour_2_temp.after(3600000,update_hourly_forecast)
        hour_3_temp.config(text=str(floor(data1["hourly"][2]["temp"])) + " ᴼ C")
        hour_3_temp.after(3600000,update_hourly_forecast)
        hour_4_temp.config(text=str(floor(data1["hourly"][3]["temp"])) + " ᴼ C")
        hour_4_temp.after(3600000,update_hourly_forecast)
        hour_5_temp.config(text=str(floor(data1["hourly"][4]["temp"])) + " ᴼ C")
        hour_5_temp.after(3600000,update_hourly_forecast)
        hour_6_temp.config(text=str(floor(data1["hourly"][5]["temp"])) + " ᴼ C")
        hour_6_temp.after(3600000,update_hourly_forecast)
        # Updating time
        hour_1.config(text=convert_time(data1["hourly"][0]["dt"]))
        hour_1.after(3600000,update_hourly_forecast)
        hour_2.config(text=convert_time(data1["hourly"][1]["dt"]))
        hour_2.after(3600000,update_hourly_forecast)
        hour_3.config(text=convert_time(data1["hourly"][2]["dt"]))
        hour_3.after(3600000,update_hourly_forecast)
        hour_4.config(text=convert_time(data1["hourly"][3]["dt"]))
        hour_4.after(3600000,update_hourly_forecast)
        hour_5.config(text=convert_time(data1["hourly"][4]["dt"]))
        hour_5.after(3600000,update_hourly_forecast)
        hour_6.config(text=convert_time(data1["hourly"][5]["dt"]))
        hour_6.after(3600000,update_hourly_forecast)
        # updating description
        hour_1_desc.config(text=data1["hourly"][0]["weather"][0]["main"].title())
        hour_1_desc.after(3600000,update_hourly_forecast)
        hour_2_desc.config(text=data1["hourly"][1]["weather"][0]["main"].title())
        hour_2_desc.after(3600000,update_hourly_forecast)
        hour_3_desc.config(text=data1["hourly"][2]["weather"][0]["main"].title())
        hour_3_desc.after(3600000,update_hourly_forecast)
        hour_4_desc.config(text=data1["hourly"][3]["weather"][0]["main"].title())
        hour_4_desc.after(3600000,update_hourly_forecast)
        hour_5_desc.config(text=data1["hourly"][4]["weather"][0]["main"].title())
        hour_5_desc.after(3600000,update_hourly_forecast)
        hour_6_desc.config(text=data1["hourly"][5]["weather"][0]["main"].title())
        hour_6_desc.after(3600000,update_hourly_forecast)

    def update_daily_forecast():
        day_1_temp.config(text=str(floor(data1["daily"][0]["temp"]["day"])) + " ᴼ C")
        day_1_temp.after(3600000,update_daily_forecast)
        day_2_temp.config(text=str(floor(data1["daily"][1]["temp"]["day"])) + " ᴼ C")
        day_2_temp.after(3600000,update_daily_forecast)
        day_3_temp.config(text=str(floor(data1["daily"][2]["temp"]["day"])) + " ᴼ C")
        day_3_temp.after(3600000,update_daily_forecast)

        day_1_desc.config(text=data1["daily"][0]["weather"][0]["main"].title())
        day_1_desc.after(3600000,update_daily_forecast)
        day_2_desc.config(text=data1["daily"][1]["weather"][0]["main"].title())
        day_2_desc.after(3600000,update_daily_forecast)
        day_3_desc.config(text=data1["daily"][2]["weather"][0]["main"].title())
        day_3_desc.after(3600000,update_daily_forecast)

    get_Weather()

    # Digital Clock Label
    digital_clock_lbl=Label(window,text="00.00",font=("ds-digital",20),bg="#0F0C29",fg="#FFFFFF")
    digital_clock_lbl.place(x=750,y=30)
    update_clock()

    # Temperature Label
    temperature_data = Label(text=str(floor(data1["current"]["temp"])) + " ᴼ C", font=("Inter SemiBold",20,"bold"), bg="#0F0C29", fg="#FFFFFF")
    temperature_data.place(x=920,y=135)
    update_temperature()

    # Weather description Label
    weather_desc_data = Label(text=data1["current"]["weather"][0]["main"].title(), font=("Inter SemiBold",20,"bold"), bg="#0F0C29", fg="#FFFFFF")
    weather_desc_data.place(x=920,y=170)
    update_weather_desc()

    # Date Label
    date = datetime.now()
    date_time_lbl = Label(window, text=f"{date:%d / %m / %Y \n%A}", font=("Inter SemiBold", 12, "bold"), bg="#FFFFFF", fg="#000000")
    date_time_lbl.place(x=600, y=30)
    update_date()

    # wind speed label
    Wind_speed_lbl = Label(window, text="Wind Speed", font= ("Inter SemiBold",12,"bold"), bg="#0575E6", fg="#FFFFFF")
    Wind_speed_lbl.place(x=150,y=180)

    # wind speed data
    wind_speed_data= Label(text= str(data1["current"]["wind_speed"]) + " meter/sec", font=("Inter SemiBold",12,"bold"), bg="#0575E6", fg="#FFFFFF")
    wind_speed_data.place(x=150,y=210)
    update_wind_speed()

    # Humidity label
    humidity_lbl = Label(window, text="Humidity", font= ("Inter SemiBold",12, "bold"), bg="#0575E6", fg="#FFFFFF")
    humidity_lbl.place(x=450,y=180)

    # Humidity data
    humidity_data = Label(text=str(data1["current"]["humidity"])+ "%", font=("Inter Regular",12,"bold"), bg="#0575E6", fg="#FFFFFF")
    humidity_data.place(x=450,y=210)
    update_humidity()

    # Pressure label
    pressure_lbl = Label(window, text="Pressure", font=("Inter Regular",12,"bold"), bg="#0575E6", fg="#FFFFFF")
    pressure_lbl.place(x=450,y=290)

    # Pressure data
    pressure_data = Label(window, text=str(data1["current"]["pressure"]) + " hPa",font=("Inter Regular",12,"bold"), bg="#0575E6", fg="#FFFFFF")
    pressure_data.place(x=450,y=320)
    update_pressure()

    # Uvi Label
    uvi_lbl = Label(window, text="UVI", font=("Inter Regular",12,"bold"), bg="#0575E6", fg="#FFFFFF")
    uvi_lbl.place(x=150,y=290)

    # Uvi data
    uvi_data = Label(window, text=data1["current"]["uvi"],font=("Inter Regular",12,"bold"), bg="#0575E6", fg="#FFFFFF")
    uvi_data.place(x=150,y=320)
    update_uvi()

    # dew point label
    dew_point_label = Label(window, text="Dew Point", font=("Inter Regular", 12, "bold"), bg="#0575E6", fg="#FFFFFF")
    dew_point_label.place(x=150, y=390)

    # dew point data
    dew_point_data = Label(window, text=str(data1["current"]["dew_point"]) + " C", font=("Inter Regular", 12, "bold"), bg="#0575E6", fg="#FFFFFF")
    dew_point_data.place(x=150, y=430)
    update_dewpoint()

    # visibility label
    visibility_label = Label(window, text="Visibility", font=("Inter Regular", 12, "bold"), bg="#0575E6", fg="#FFFFFF")
    visibility_label.place(x=450, y=390)

    # visibility data
    visibility_data = Label(window, text=str(data1["current"]["visibility"]) + " meter", font=("Inter Regular", 12, "bold"), bg="#0575E6", fg="#FFFFFF")
    visibility_data.place(x=450, y=430)
    update_visibility()

    # Adding sunrise label
    sunrise_label = Label(window, text="Sunrise", font=("Inter Regular", 12, "bold"), bg="#FFFFFF", fg="#000000")
    sunrise_label.place(x=750, y=480)

    # Sunrise data label
    sunrise_label = Label(window, text=convert_time(data1["current"]["sunrise"]), font=("Inter Regular", 12, "bold"), bg="#FFFFFF", fg="#000000")
    sunrise_label.place(x=750, y=510)

    # Adding sunset label
    sunset_label = Label(window, text="Sunset", font=("Inter Regular", 12, "bold"), bg="#FFFFFF", fg="#000000")
    sunset_label.place(x=750, y=580)

    # Sunset data label
    sunset_data = Label(window, text=convert_time(data1["current"]["sunset"]), font=("Inter Regular", 12, "bold"), bg="#FFFFFF", fg="#000000")
    sunset_data.place(x=750, y=600)

    # Hourly Forecast
    # Hour 1 label
    hour_1 = Label(window, text=convert_time(data1["hourly"][0]["dt"]), font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_1.place(x=55, y=510)

    # hour 2 Label
    hour_2 = Label(window, text=convert_time(data1["hourly"][1]["dt"]), font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_2.place(x=170, y=510)

    # Hour 3 label
    hour_3 = Label(window, text=convert_time(data1["hourly"][2]["dt"]), font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_3.place(x=285, y=510)

    # Hour 4 label
    hour_4 = Label(window, text=convert_time(data1["hourly"][3]["dt"]), font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_4.place(x=390, y=510)

    # Hour 5 label
    hour_5 = Label(window, text=convert_time(data1["hourly"][4]["dt"]), font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_5.place(x=495, y=510)

    # Hour 6 label
    hour_6 = Label(window, text=convert_time(data1["hourly"][5]["dt"]), font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_6.place(x=600, y=510)

    # hour 1 temperature
    hour_1_temp = Label(window, text=str(floor(data1["hourly"][0]["temp"])) + " ᴼ C", font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_1_temp.place(x=55, y=550)

    # hour 2 temperature
    hour_2_temp = Label(window, text=str(floor(data1["hourly"][1]["temp"])) + " ᴼ C", font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_2_temp.place(x=170, y=550)

    # hour 3 temperature
    hour_3_temp = Label(window, text=str(floor(data1["hourly"][2]["temp"])) + " ᴼ C", font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_3_temp.place(x=285, y=550)

    # hour 4 temperature
    hour_4_temp = Label(window, text=str(floor(data1["hourly"][3]["temp"])) + " ᴼ C", font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_4_temp.place(x=390, y=550)

    # hour 5 temperature
    hour_5_temp = Label(window, text=str(floor(data1["hourly"][4]["temp"])) + " ᴼ C", font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_5_temp.place(x=495, y=550)

    # hour 6 temperature
    hour_6_temp = Label(window, text=str(floor(data1["hourly"][5]["temp"])) + " ᴼ C", font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_6_temp.place(x=600, y=550)

    # hour 1 description
    hour_1_desc = Label(window, text=data1["hourly"][0]["weather"][0]["main"], font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_1_desc.place(x=55, y=590)

    # hour 2 description
    hour_2_desc = Label(window, text=data1["hourly"][1]["weather"][0]["main"], font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_2_desc.place(x=170, y=590)

    # hour 3 description
    hour_3_desc = Label(window, text=data1["hourly"][2]["weather"][0]["main"], font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_3_desc.place(x=285, y=590)

    # hour 4 description
    hour_4_desc = Label(window, text=data1["hourly"][3]["weather"][0]["main"], font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_4_desc.place(x=390, y=590)

    # hour 5 description
    hour_5_desc = Label(window, text=data1["hourly"][4]["weather"][0]["main"], font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_5_desc.place(x=495, y=590)

    # hour 6 description
    hour_6_desc = Label(window, text=data1["hourly"][5]["weather"][0]["main"], font=("Inter Regular", 12, "bold"), bg="#41295A", fg="#FFFFFF")
    hour_6_desc.place(x=600, y=590)

    update_hourly_forecast()

    # Overview label
    overview_label = Label(window, text=" Today Overview", font=("Inter Regular", 15, "bold"), bg="#FFFFFF", fg="#000000")
    overview_label.place(x=110, y=70)

    # Day 1 label
    day_1 = Label(window, text=convert_day(data1["daily"][0]["dt"]), font=("Inter Regular", 12, "bold"), bg="#0F0C29", fg="#FFFFFF")
    day_1.place(x=745, y=270)

    # day 2 label
    day_2 = Label(window, text=convert_day(data1["daily"][1]["dt"]), font=("Inter Regular", 12, "bold"), bg="#0F0C29", fg="#FFFFFF")
    day_2.place(x=745, y=330)

    # Day 3 label
    day_3 = Label(window, text=convert_day(data1["daily"][2]["dt"]), font=("Inter Regular", 12, "bold"), bg="#0F0C29", fg="#FFFFFF")
    day_3.place(x=745, y=390)

    # day 1 temperature
    day_1_temp = Label(window, text=str(floor(data1["daily"][0]["temp"]["day"])) + " ᴼ C", font=("Inter Regular", 12, "bold"), bg="#0F0C29", fg="#FFFFFF")
    day_1_temp.place(x=910, y=270)

    # day 2 temperature
    day_2_temp = Label(window, text=str(floor(data1["daily"][1]["temp"]["day"])) + " ᴼ C", font=("Inter Regular", 12, "bold"), bg="#0F0C29", fg="#FFFFFF")
    day_2_temp.place(x=910, y=330)

    # day 3 temperature
    day_3_temp = Label(window, text=str(floor(data1["daily"][2]["temp"]["day"])) + " ᴼ C", font=("Inter Regular", 12, "bold"), bg="#0F0C29", fg="#FFFFFF")
    day_3_temp.place(x=910, y=390)

    # day 1 desc label
    day_1_desc = Label(window, text=data1["daily"][0]["weather"][0]["main"], font=("Inter Regular", 12, "bold"), bg="#0F0C29", fg="#FFFFFF")
    day_1_desc.place(x=910, y=290)

    # day 2 desc label
    day_2_desc = Label(window, text=data1["daily"][1]["weather"][0]["main"], font=("Inter Regular", 12, "bold"), bg="#0F0C29", fg="#FFFFFF")
    day_2_desc.place(x=910, y=350)

    # day 3 desc
    day_3_desc = Label(window, text=data1["daily"][2]["weather"][0]["main"], font=("Inter Regular", 12, "bold"), bg="#0F0C29", fg="#FFFFFF")
    day_3_desc.place(x=910, y=410)

    update_daily_forecast()
    # location
    state_country = Label(window, text=str(location[0]), font=("Inter Regular", 12, "bold"), bg="#0F0C29", fg="#FFFFFF")
    state_country.place(x=750, y=70)

    # icon id
    icon_id = data1["current"]["weather"][0]["icon"]

    # icon url
    icon_url = "http://openweathermap.org/img/wn/" + icon_id + ".png"

    # Downloading icon image
    urllib.request.urlretrieve(icon_url, "icon.png")

    # Defining icon image
    logo = PhotoImage(file="icon.png")
    logo_label = Label(window, image=logo)
    logo_label.place(x=770, y=140)

    # sunrise icon 
    sunrise = PhotoImage(file="assets/sunrise.png")
    sunrise_icon = Label(window, image=sunrise)
    sunrise_icon.place(x=930, y=485)

    # sunset icon 
    sunset = PhotoImage(file="assets/sunset.png")
    sunset_icon = Label(window, image=sunset)
    sunset_icon.place(x=930, y=575)

    # app icon 
    app_icon = PhotoImage(file="assets/logo.png")
    app_logo = Label(window, image=app_icon)
    app_logo.place(x=10, y=25)

    # Right side rectangle with time, temp, location, 3 days forecast, sunrise, sunset
    canvas.create_rectangle(
        715.0,
        0.0,
        1035.0,
        665.0,
        fill="#0F0C29",
        outline="")

    # Today Details box
    canvas.create_rectangle(
        0.0,
        125.0,
        715.0,
        665.0,
        fill="#0575E6",
        outline="")

    # Line below tempearture
    canvas.create_rectangle(
        742.0,
        230.0,
        1007.0,
        231.0,
        fill="#D2AD2B",
        outline="")


    # Line below Today Overview
    canvas.create_rectangle(
        121.0,
        104.98539733886719,
        260.99989318847656,
        107.0,
        fill="#000000",
        outline="")

    # sun rise box
    canvas.create_rectangle(
        735.0,
        472.0,
        1024.0,
        549.0,
        fill="#FFFFFF",
        outline="")


    # sunset box
    canvas.create_rectangle(
        735.0,
        566.0,
        1024.0,
        643.0,
        fill="#FFFFFF",
        outline="")


    # hourly forecast box
    canvas.create_rectangle(
        23.0,
        479.0,
        696.0,
        643.0,
        fill="#41295A",
        outline="")

except:
    # Error message
    error = Label(window, text="Error: Please check your internet connection", font=("Inter Regular", 20, "bold"), bg="#FFFFFF", fg="#000000")
    error.place(x=300, y=300)

window.resizable(False, False)
window.mainloop()
