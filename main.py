import openpyxl
from program import pg

excel = 'JUEGOS.xlsx'
DIR = '/home/matito/Downloads/'
CON = 'GBA'

wb_obj = openpyxl.load_workbook(excel)
sheet_obj = wb_obj.active
max_row = sheet_obj.max_row
#for i in range(2, max_row):
    #GAME = sheet_obj.cell(row=i,column=1)
    #if GAME.value == None:
        #exit()
    #else:
        #print(GAME.value, i)
        #pg(GAME.value,DIR,CON)
pg("Castlevania harmony of despair",DIR,CON)
pg("mario kart",DIR,CON)