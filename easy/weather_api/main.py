import requests as req
from dotenv import load_dotenv
from datetime import datetime
import os
from rich import print
import sys


load_dotenv()   # load API_KEY from environment

def main():
    city = "Prague"
    API_KEY = os.getenv("API_KEY")
    try:
        city = sys.argv[1]
    except:
        city = input("Enter city: ")
        print("\n")
    
    try:
        res = req.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
    except req.exceptions.ConnectionError:
        print("No network connection")
        sys.exit()
    if res.status_code == 200:
        printTable(res.json())
    else:
        print(f"No data found for {city}")
    

def printTable(data):
    main = data['main']
    print("┌────────────── Weather Report ──────────────┐")
    print(f"  City: {data['name']}", )
    print("├ 🌡️ [bold]Temperature[/bold] ───────────────────────────┤")
    print(f"     ├─Current: {main['temp']}°C")
    print(f"     ├─Min: {main['temp_min']}°C")
    print(f"     ├─Max: {main['temp_max']}°C")
    print(f"     └─Feels like: {main['feels_like']}°C")

    print("├ 💨 [bold]Other[/bold] ─────────────────────────────────┤")
    print(f"     ├─Humidity: {main['humidity']}%")
    print(f"     ├─Wind speed: {data['wind']['speed']} m/s")
    print(f"     └─Clouds: {data['clouds']['all']}%")
    print("├ ☀️ [bold]Sun[/bold] ───────────────────────────────────┤")
    print(f"     ├─Sunrise: {datetime.fromtimestamp(int(data['sys']['sunrise'])).strftime("%H:%M")}")
    print(f"     └─Sunset: {datetime.fromtimestamp(int(data['sys']['sunset'])).strftime("%H:%M")}")

    print("└────────────────────────────────────────────┘")
    
if __name__ == "__main__":
    main()