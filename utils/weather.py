import requests

API_KEY = "your_openweather_api_key"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"Weather in {city}: {weather}, {temp}°C"
    else:
        return "City not found or API issue."

