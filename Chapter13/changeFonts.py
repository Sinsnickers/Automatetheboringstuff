import openpyxl, os
from openpyxl.styles import Font

os.chdir("Chapter13")
wb = openpyxl.Workbook()
sheet =wb["Sheet"]
italic24Font = Font(size = 24, italic = True)
sheet["A1"].font = italic24Font
sheet["A1"] = "Hello suckers"
fontObj1 = Font(name='Times New Roman', bold=True)
sheet['A2'].font = fontObj1
sheet['A2'] = 'Bold Times New Roman'

fontObj2 = Font(size=24, italic=True)
sheet['A3'].font = fontObj2
sheet['A3'] = '24 pt Italic'
wb.save("styles.xlsx")
