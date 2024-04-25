#!/usr/bin/python3

import requests

url = "https://search.imdbot.workers.dev"

print("BIENVENIDO AL BUSCADOR DE PELICULAS")

title = input("Pon el titulo de la pelicula: ")

url = url + '/?q=' + title

film = requests.get(url)

peli = film.json()

print(f"Titulo: ", peli['description'][0]['#TITLE'], '\n', "Año: ", peli['description'][0]['#YEAR'], '\n', "Actores: ", peli['description'][0]['#ACTORS'])


