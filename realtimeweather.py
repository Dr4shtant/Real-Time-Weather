import requests

def get_weather(city, api_key):
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
        latitude = data['coord']['lon']
        longitude = data['coord']['lat']
        pressure = data['main']['pressure']
        
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} bar")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")

    else:
        print("Error:", data.get("message", "Unable to fetch weather data"))

# Add your OpenWeatherMap API key in api_key
api_key = 'f00275629d357c3e1df2ccbd6b2c2e77'
city = input("Enter the city name: ")
get_weather(city, api_key)
