#!/usr/bin/python3

import subprocess
import gspread

dmesg = subprocess.getoutput("dmesg")

dmesg_data = []

for dmesg_line in dmesg.splitlines():
	dmesg_temp = dmesg_line.split("[")[1]
	dmesg_time = dmesg_temp.split("]")[0]
	dmesg_temp = dmesg_temp.split("]")[1]
	dmesg_temp = dmesg_temp.split(":")
	dmesg_module = dmesg_temp[0]
	dmesg_info = ""

	if len(dmesg_temp) > 1:
		dmesg_info = dmesg_temp[1]
	
	dmesg_data.append([dmesg_time, dmesg_module, dmesg_info])

gc = gspread.service_account()
sh = gc.open("dmesg_log")

date = subprocess.getoutput("date +%Y%m%d")

worksheet_list = sh.worksheets()

exist = False
for sheet in worksheet_list:
	print(sheet.title)
	if sheet.title == date:
		sh.worksheet(date).clear()
		exist = True
if exist == False:
	sh.add_worksheet(title=date, rows=1000, cols=3)
sh.worksheet(date).append_rows(dmesg_data)
