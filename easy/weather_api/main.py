import requests as req
from dotenv import load_dotenv
import os
import json
load_dotenv()   # load API_KEY from environment

def main():
    city = "Prague"
    API_KEY = os.getenv("API_KEY")

    res = req.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}")
    data = res.json()
    print(json.dumps(data, indent=1))
    print("City:", data[])

if __name__ == "__main__":
    main()