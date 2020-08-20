#! python3
# renameDates.py - rename american dates MM-DD-YYYY to european dates DD-MM-YYYY

import shutil, os, re

#Create a regex that fits american datetypes
datePattern = re.compile(f""" 
    ^(.*?)              # all text before the date
    ((0|1)?\d)-         # matches 2 digits with 0 or 1 first digit  
    ((0|1|2|3)?\d)-     # matches 2 digits with 0-3 first digit   
    ((19|20)\d\d)      # matches 4 digits with 19-20 first 2 digits
    (.*?)$             # all text after the date            
    """,re.VERBOSE)

#Loop over files in workind directory
for amerFilename in os.listdir():
    mo = datePattern.search(amerFilename)

#skip files that are none
    if mo == None:
        continue

#get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8) 
#Form european-style form filename
    euroFilename = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart

#Get the full absolute filepaths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

# Rename the files.
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    #shutil.move(amerFilename, euroFilename)   # uncomment after testing