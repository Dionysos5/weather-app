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
        weather_data = api.get_weather(city)
        print(f"Weather in {city}:")
        print(f"{weather_data['temperature']}°C with {weather_data['description']}")
        see_hourly = input("Would you like to see the forecast? (y/n): ")
        if see_hourly.lower() == "y":
            response = api.get_five_day_forecast(city)
            print("-----------------")
            for day in response:
                print(f"{day['date']}")
                for forecast in day["forecast"]:
                    print(f"\t{forecast['time']}H \t {forecast['temperature']}°C \t {forecast['description']}")
        else:
            print("Thank you for using the weather app!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()