#!/usr/bin/python3

import gspread
import subprocess

gc = gspread.service_account()
sh = gc.open("dmesg_log")

worksheet_list = sh.worksheets()

print("BIENVENIDO A MI CONSULTORA")

print("Que log de los ultimos 5 dias quieres ver?")

num_sheet = len(worksheet_list)

num_sheet_ini = num_sheet - 5

top_five = 0

for sheet in worksheet_list:
	if num_sheet_ini <= top_five:
		print(sheet.title)
	top_five = top_five + 1

verify = False

while verify == False:
	user_day = input("Escoge la que dia quieres ver: ")

	for sheet in worksheet_list:
		if num_sheet_ini <= top_five:
			if user_day == sheet.title:
				verify = True

	if verify == False:
		print("ESCOGE UN DIA DISPONIBLE!!!")

print("Quieres hacer?")
print("1- Copia de seguridad")
print("2- Buscar por palabra")

option = input("Escoge una opcion con el numero: ")

if int(option) == 2:
	user_word = input("Que palabra quieres buscar: ")
	
	day = sh.worksheet(user_day)
	time = day.col_values(1)
	module = day.col_values(2)
	message = day.col_values(3)

	pos = module.index(' '+user_word)
	
	print(time[pos],module[pos],message[pos])

