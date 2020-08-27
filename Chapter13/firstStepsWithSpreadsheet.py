import openpyxl,os
    #Change current working directory to find excel-file
os.chdir("C:\\Users\\bero8\\BoringStuff\\Automatetheboringstuff\\automate_online-materials")
    #Opening Excel Documents with OpenPyXL
wb = openpyxl.load_workbook("example.xlsx")
print(type(wb))
print("---------------------------------------------")
    #Getting Sheets from the Workbook
print(wb.sheetnames)
print("---------------------------------------------")
sheet = wb["Sheet1"]
print(sheet)
print(sheet.title)
print("---------------------------------------------")
anotherSheet = wb.active
print(anotherSheet)
print("---------------------------------------------")
    #Getting Cells from the Sheets
print(sheet["A1"])
print(sheet["A1"].value)
print("---------------------------------------------")
cell = sheet["B1"]
cellValue = cell.value
print(cell)
print(cellValue)
print("---------------------------------------------")
print(f"Row {cell.row}, from column {cell.column} is {cell.value}")
print("---------------------------------------------")
print("---------------------------------------------")