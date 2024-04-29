import os
from dotenv import load_dotenv
from datetime import datetime
from api_request import APIRequest

load_dotenv()

class OpenWeatherMapAPI:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        self.base_url = os.getenv("OPENWEATHERMAP_API_BASE_URL")
        self.weather_endpoint = "data/2.5/weather"
        self.forecast_endpoint = "data/2.5/forecast"
        self.geo_endpoint = "geo/1.0/direct"
        self.api_request = APIRequest(self.base_url, self.api_key)

    def get_weather(self, city: str):
        data = self.api_request.make_request(self.weather_endpoint, {"q": city, "units": "metric"})
        if "name" in data and "main" in data and "weather" in data:
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
            }
        else:
            raise ValueError("Weather data is incomplete")

    def get_lat_lon(self, city: str):
        data = self.api_request.make_request(self.geo_endpoint, {"q": city, "limit": 1})[0]
        return {"lat": data["lat"], "lon": data["lon"]}
    
    def get_five_day_forecast(self, lat:float, lon:float):
        nb_timestamps = 8
        data = self.api_request.make_request(self.forecast_endpoint, {"lat": lat, "lon": lon, "cnt": nb_timestamps, "units": "metric", "lang": "fr"})
        # Extract the hourly forecast information
        hourly_forecast = []
        for forecast in data["list"]:
            hourly_forecast.append({
                "time": datetime.fromtimestamp(forecast["dt"]).strftime("%Y-%m-%d %H:%M:%S"),
                "temperature": forecast["main"]["temp"],
                "description": forecast["weather"][0]["description"],
            })
        return hourly_forecast