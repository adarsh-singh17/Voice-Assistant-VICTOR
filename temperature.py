import os
import sys
import requests


################################                                 Function to get temperature                                 ###############################

def get_temperature(city):
    api_key = os.getenv("Weather_api_key")
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    
    if data.get("main") and data.get("weather"):
        main = data["main"]
        temperature = main["temp"]
        humidity = main["humidity"]
        pressure = main["pressure"]
        weather_description = data["weather"][0]["description"]
        return temperature, humidity, pressure, weather_description
    else:
        return None, None, None, "Sorry, I couldn't retrieve the weather information."

