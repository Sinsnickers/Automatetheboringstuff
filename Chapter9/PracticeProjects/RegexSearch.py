#! python3
#RegexSearch opens all txt.files in a folder and searches
#for any line that matches user-supplied regular expression

import re, os
from pathlib import Path

#TODO
#ask user for folder to open
#searchFolder = input("Enter the absolute path you want to search through\n")
os.chdir("c:/Users/bero8/BoringStuff/Automatetheboringstuff/Chapter9/PracticeProjects")
currentFolder = Path.cwd()

#TODO
#ask user for his regular expression
userinput = input("What regex do you want to search\n")
regexSearch = re.compile(rf"{userinput}")

#TODO
#open all txt.files in this folder
for textFile in currentFolder.glob("*.txt"):
    searchFile = open(textFile,"r")
    for line in searchFile:
        #search through all txt.files for match of the re
        result = regexSearch.findall(line)
        if result != []:
            #print result to screen
            print(result)
    searchFile.close()