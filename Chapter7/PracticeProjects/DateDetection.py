#! Python3
import re, pyperclip
def isLeapYear(year): # returns True if the year is a leap year
    year = year
    isValid = False
    if year % 4 == 0: 
        isValid = True
        if year % 4 == 0 and year % 100 == 0:
            isValid = False
            if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
                isValid = True
    return isValid

# Create Regex for date like input 
dateRegex = re.compile(r"""
    ((\d{2})   # 1 or 2 digits
    /           # forward slash
    (\d{2})   # 1 or 2 digits
    /           #forward slash
    (\d{4}))   # 4 digits
    """,re.X)

text = pyperclip.paste() # take text to search in variable
testDate = dateRegex.findall(text)

monthsWith30Days = [4,6,9,11]
validDates = []
for i in range(len(testDate)):
    for j in range(1,4):
        try:
            day = testDate[i][j]
            month = testDate[i][j+1]
            year = testDate[i][j+2]
            while testDate is not None:
                if int(year) < 1000 or int(year) > 2999:
                    break
                elif int(month) > 12:
                    break
                elif int(day) > 31:
                    break
                elif int(day) == 31 and int(month) in monthsWith30Days:
                    break
                elif int(day) > 29 and int(month) == 2:
                    break
                elif int(day) == 29 and int(month) == 2 and isLeapYear(int(year))==False:
                    break
                else:
                    validDates.append(testDate[i][0])
                    break
        except:
            continue

for date in validDates:
    pyperclip.copy("\n".join(validDates))

