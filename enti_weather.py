#!/usr/bin/python3

import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=41.4&longitude=2.12&current=temperature_2m,wind_speed_10m"

weather = requests.get(url)

w = weather.json()

print("La temperatura en ENTI es: "+str(w['current']['temperature_2m']))
