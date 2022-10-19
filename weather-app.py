import tkinter as tk
from tkinter import *
import requests
import geocoder
import time
import json
from datetime import datetime

root = Tk()
root.title("Weather Now")
root.geometry("1500x800")
root.resizable(False,False)

def update_status():
    status_lbl.config(text = "Unable to Refresh...")

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

    def update_temperature():
        temperature_data.config(text=str(data1["current"]["temp"]) + " C")
        temperature_data.after(100,update_temperature)

    def update_humidity():
        humidity_data.config(text=data1["current"]["humidity"])
        humidity_data.after(100,update_humidity)

    def update_wind_speed():
        wind_speed_data.config(text=data1["current"]["wind_speed"])
        wind_speed_data.after(100,update_wind_speed)

    def update_weather_desc():
        weather_desc_data.config(text=data1["current"]["weather"][0]["main"].title())
        weather_desc_data.after(100,update_weather_desc)

    def update_time_zone():
        time_zone_data.config(text=data1["timezone"])
        time_zone_data.after(100,update_time_zone)

    def update_feelslike():
        feelslike_data.config(text=data1["current"]["feels_like"])
        feelslike_data.after(100,update_feelslike)

    def update_pressure():
        pressure_data.config(text=data1["current"]["pressure"])
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
    update_status()

getWeather()
# search box
Search_image = PhotoImage(file="search.png")
image_search_bar = Label(image=Search_image)
image_search_bar.place(x=1000,y=20)

# Text Field for city
text_field = tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
text_field.place(x=1050,y=40)
text_field.focus()

# Search Icon
Search_icon = PhotoImage(file="search_icon.png")
image_search_icon = Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040")
image_search_icon.place(x=1370,y=25)

# Logo Image
logo_image = PhotoImage(file="weather.png") # Done ########################################
logo = Label(image=logo_image)
logo.place(x=150,y=100)

#label
status_lbl = Label(root, text="online", fg = "green", font=("poppins",10,"bold"))
status_lbl.place(x=600,y=10)

digital_clock_lbl=Label(root,text="00.00.00",font=("ds-digital",20),fg="#404040")
digital_clock_lbl.place(x=100,y=50)
update_clock()

date = datetime.now()
date_time_lbl = Label(root, text=f"{date:%d / %m / %Y\n%A}", font=("poppins", 10))  # Done ########################################
date_time_lbl.place(x=140,y=85)
update_date()

temperature_data = Label(text=str(data1["current"]["temp"]) + " C", font=("arial",60,"bold"))
temperature_data.place(x=850, y=200)
update_temperature()

time_zone_data = Label(text=data1["timezone"], font=("arial",20,"bold"))
time_zone_data.place(x=850, y=310)
update_time_zone()

weather_desc_data = Label(text=data1["current"]["weather"][0]["main"].title(), font=("arial",20,"bold"))
weather_desc_data.place(x=850, y=370)
update_weather_desc()

Wind_speed_lbl = Label(root, text="WIND", font= ("arial",15, "bold"),fg = "#404040")
Wind_speed_lbl.place(x=120, y= 650)

wind_speed_data= Label(text= data1["current"]["wind_speed"], font=("arial",20,"bold"))
wind_speed_data.place(x=120, y=700)
update_wind_speed()

humidity_lbl = Label(root, text="HUMIDITY", font= ("poppins",15, "bold"),fg = "#404040")
humidity_lbl.place(x=350, y= 650)

humidity_data = Label(text=data1["current"]["humidity"], font=("arial",20,"bold"))
humidity_data.place(x=350, y=700)
update_humidity()

feelslike_lbl = Label(root, text="FELLS LIKE", font=("arial",15,"bold"),fg="#404040")
feelslike_lbl.place(x=600,y=650)

feelslike_data = Label(root, text=data1["current"]["feels_like"],font=("arial",20,"bold"))
feelslike_data.place(x=600,y=700)
update_feelslike()

pressure_lbl = Label(root, text="PRESSURE", font=("arial",15,"bold"),fg="#404040")
pressure_lbl.place(x=850,y=650)

pressure_data = Label(root, text=data1["current"]["pressure"],font=("arial",20,"bold"))
pressure_data.place(x=850,y=700)
update_pressure()

uvi_lbl = Label(root, text="UVI", font=("arial",15,"bold"),fg="#404040")
uvi_lbl.place(x=1120,y=650)

uvi_data = Label(root, text=data1["current"]["uvi"],font=("arial",20,"bold"))
uvi_data.place(x=1100,y=700)
update_uvi()

root.mainloop()