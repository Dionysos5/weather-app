from urllib.parse import quote_plus
from open_weather_api import OpenWeatherMapAPI

def main():
    api = OpenWeatherMapAPI()

    while True:
        city = quote_plus(input("Enter a city name: ").strip())
        if city:
            break
        print("City must be a non-empty string. Please try again!")

    try:
        lat_lon = api.get_lat_lon(city)
        print(f"The latitude and longitude of {city} are {lat_lon['lat']} and {lat_lon['lon']} respectively.")
        weather_data = api.get_weather(city)
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Description: {weather_data['description']}")
        see_hourly = input("Would you like to see the forecast? (y/n): ")
        if see_hourly.lower() == "y":
            hourly_forecast = api.get_five_day_forecast(lat_lon["lat"], lat_lon["lon"])
            print("Forecast:")
            for forecast in hourly_forecast:
                print(f"Time: {forecast['time']}, Temperature: {forecast['temperature']}°C, Description: {forecast['description']}")
        else:
            print("Thank you for using the weather app!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()