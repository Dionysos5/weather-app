import os
import requests
from dotenv import load_dotenv
from urllib.parse import quote_plus
from datetime import datetime


# Load the environment variables
load_dotenv()

# Get the API key from the environment variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL")

def get_weather(city):
    # Get the weather data from the OpenWeatherMap API
    encoded_city = quote_plus(city)
    url = f"{API_BASE_URL}/weather?q={encoded_city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    # Extract the weather information
    weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
    }
    return weather

def get_lat_lon(city):
    # Get the latitude and longitude of the city
    encoded_city = quote_plus(city)

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={encoded_city }&limit=1&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()[0]
    # Extract the latitude and longitude
    lat_lon = {
        "lat": data["lat"],
        "lon": data["lon"]
    }
    return lat_lon

def get_five_day_forecast(lat, lon):
    nb_timestamps = 8
    url = f"{API_BASE_URL}/forecast?lat={lat}&lon={lon}&appid={API_KEY}&cnt={nb_timestamps}&units=metric&lang=fr"
    response = requests.get(url)
    data = response.json()

    # Extract the hourly forecast information
    hourly_forecast = []
    for forecast in data["list"]:
        hourly_forecast.append({
            "time": datetime.fromtimestamp(forecast["dt"]).strftime("%Y-%m-%d %H:%M:%S"),
            "temperature": forecast["main"]["temp"],
            "description": forecast["weather"][0]["description"],
        })
    return hourly_forecast

def main():
    city = input("Enter the city name: ")
    lat_lon = get_lat_lon(city)
    print(f"The latitude and longitude of {city} are {lat_lon['lat']} and {lat_lon['lon']} respectively.")
    weather = get_weather(city)
    print(f"The temperature in {weather['city']} is {weather['temperature']}°C with {weather['description']}.")
    see_hourly = input("Would you like to see the forecast? (y/n): ")
    if see_hourly.lower() == "y":
        hourly_forecast = get_five_day_forecast(lat_lon["lat"], lat_lon["lon"])
        print("Forecast:")
        for forecast in hourly_forecast:
            print(f"Time: {forecast['time']}, Temperature: {forecast['temperature']}°C, Description: {forecast['description']}")
    else:
        print("Thank you for using the weather app!")

if __name__ == "__main__":
    main()