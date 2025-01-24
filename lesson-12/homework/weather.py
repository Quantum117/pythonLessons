import requests


API_KEY = '8f9324e53a2c2702566a21c3436aeb0a'

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Define the city and parameters
city = input("enter city name:").strip()
params = {
    'q': city,           # City name
    'appid': API_KEY,    # Your API key
    'units': 'metric'    # Units: metric for Celsius, imperial for Fahrenheit
}

# Make a GET request
response = requests.get(BASE_URL, params=params)

# Check the response status show detailed error message

if response.status_code == 200:
    # Parse JSON data
    data = response.json()
    print(f"Weather in {city}: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
else:
    print(f"Error: {response.status_code}")
    print(response.json())  # Optional: