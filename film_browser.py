#!/usr/bin/python3

import requests
import gspread

url = "https://search.imdbot.workers.dev"

print("BIENVENIDO AL BUSCADOR DE PELICULAS")

title = input("Pon el titulo de la pelicula: ")

url = url + '/?q=' + title
film = requests.get(url)
peli = film.json()

error = peli['description']

title = peli['description'][0]['#TITLE']
year = peli['description'][0]['#YEAR']
actors = peli['description'][0]['#ACTORS']
if len(error) == 0:  
	print("ERROR: titulo no encontrado")
else:
	print(f"Titulo: ", title, '\n', "Año: ", year, '\n', "Actores: ", actors)

gc = gspread.service_account()

sh = gc.open("pelis")

sh.sheet1.append_row([title,year,actors])
