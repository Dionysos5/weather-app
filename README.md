# CLI Weather App

## Introduction

This project is designed as a learning exercise to explore Python programming. It is a command-line interface (CLI) weather application that allows users to retrieve weather information.

## Current Features

- **Get Current Weather**: Users can retrieve the current weather conditions for any specified city.
- **Get Weather Forecast**: Users can also obtain weather forecasts for a city, including future temperature and weather conditions.

## Future Features

- **Fuzzy Search**: Implement fuzzy search for city names if the city is not found and let user select a city.

## Getting Started

To use this application, follow these steps:

1. Clone the repository:
   ```bash
   git clone git@github.com:Dionysos5/weather-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd yourrepository
   ```
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source .venv/bin/activate
     ```
5. Set up environment variables:

   - Create a file named .env in the root of the project directory.
   - Add the following content to the .env file:

   ```bash
   OPENWEATHERMAP_API_BASE_URL=https://api.openweathermap.org/data/2.5
   OPENWEATHERMAP_API_KEY=your_api_key_here
   ```

   Replace `your_api_key_here` with your actual OpenWeatherMap API key, which you can obtain by registering on the OpenWeatherMap website.

6. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
7. Run the application:
   ```bash
   python main.py
   ```
