import openpyxl, os

os.chdir("Chapter13")

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active
sheet.freeze_panes = 'A2' # Freeze the rows above A2.
wb.save('freezeExample.xlsx')