#!/usr/bin/python3

import gspread

gc = gspread.service_account()

sh = gc.open("prueba_api")

print(sh.sheet1.get('A1'))
