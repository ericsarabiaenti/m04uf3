#!/usr/bin/python3

import requests

url = "https://search.imdbot.workers.dev"

print("BIENVENIDO AL BUSCADOR DE PELICULAS")

title = input("Pon el titulo de la pelicula: ")

url = url + '/?q=' + title
film = requests.get(url)
peli = film.json()

error = peli['description']

if len(error) == 0:  
	print("ERROR: titulo no encontrado")
else:
	print(f"Titulo: ", peli['description'][0]['#TITLE'], '\n', "Año: ", peli['description'][0]['#YEAR'], '\n', "Actores: ", peli['description'][0]['#ACTORS'])


