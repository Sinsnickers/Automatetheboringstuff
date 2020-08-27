import openpyxl,os

os.chdir("automate_online-materials")

wb = openpyxl.load_workbook("example.xlsx")
print(wb.sheetnames)
sheet = wb["Sheet1"]
print(tuple(sheet['A1':'C3']))
print("-------------------------------------------")
for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')
print("-------------------------------")
sheet = wb.active
list(sheet.columns)[1] # Get second column's cells.
for cellObj in list(sheet.columns)[1]:
    print(cellObj.value)