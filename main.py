import openpyxl
from program import pg

excel = 'JUEGOS.xlsx'
DIR = '/home/matito/Downloads/'
CON = 'GBA'

wb_obj = openpyxl.load_workbook(excel)
sheet_obj = wb_obj.active
max_row = sheet_obj.max_row
for i in range(2, max_row):
    GAME = sheet_obj.cell(row=i,column=1)
    if GAME.value == None:
        exit()
    else:
        print(i-1,GAME.value)
        not_found = pg(GAME.value,DIR,CON)
        if(not_found):
            continue
        