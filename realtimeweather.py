import requests
import os

def get_weather(city):
    api_key = os.getenv('OPENWEATHER_API_KEY')  # Gets the API key from environment variables
    if not api_key:
        raise ValueError("No API key found in environment variables. Please set the OPENWEATHER_API_KEY environment variable.")

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use imperial for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        pressure = data['main']['pressure']
        
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    else:
        print("Error:", data.get("message", "Unable to fetch weather data"))


city = input("Enter the city name: ")
get_weather(city)
