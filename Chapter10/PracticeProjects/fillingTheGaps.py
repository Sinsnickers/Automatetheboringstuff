#!python3
#fillingTheGaps.py- searches for files in a folder and
#looks for gaps, spam001 spam002 spam004 and renames the files

import os, shutil, re
from pathlib import Path

#changes the current working directiory as the users want 
os.chdir(r"c:\\users\\bero8\\testFolder")
currentFolder = Path.cwd()
numberRegex = re.compile(f"""
    (\w+)(\d\d\d)
    (\.txt)
""",re.X)

#iterate over all files in this folder
currentNumber = 0
for filename in os.listdir(currentFolder):
    spamFile = numberRegex.search(filename)
    wordPart = spamFile.group(1)
    numberPart = spamFile.group(2)
    if f"{currentNumber:03}" == numberPart:
        pass
    else:
        shutil.move(filename,wordPart+f"{currentNumber:03}.txt")
    currentNumber = currentNumber + 1
    #search for gaps in filename

















#for i in range(50):
    #spam = open(f"spam{i:03}.txt","w")
    #spam.close

#for i in range(60,100):
    #spam = open(f"spam{i:03}.txt","w")
    #spam.close