import os
import requests
from dotenv import load_dotenv
from urllib.parse import quote_plus


# Load the environment variables
load_dotenv()

# Get the API key from the environment variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL")

def get_weather(city):
    # Get the weather data from the OpenWeatherMap API
    encoded_city = quote_plus(city)
    url = f"{API_BASE_URL}?q={encoded_city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    # Extract the weather information
    weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
    }
    return weather

def main():
    city = input("Enter the city name: ")
    weather = get_weather(city)
    print(f"The temperature in {weather['city']} is {weather['temperature']}°C with {weather['description']}.")

if __name__ == "__main__":
    main()