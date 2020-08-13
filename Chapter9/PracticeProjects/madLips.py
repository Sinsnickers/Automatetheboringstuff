#! python3
#MadLips.py - search a text file and replaces asked
#words. Prints the new text to screen and saves it in new txt.file

import pyperclip, pathlib as Path, re, sys
#TODO open text file
try:
    textFile = open(sys.argv[1],"r")
    text = textFile.read()
    textFile.close()
    #print("Enter new file name")
    #newFile = open(input(),"w")
    wordRegex = re.compile(r"(ADJECTIVE)|(NOUN)|(VERB)|(ADVERB)")
    searchText = wordRegex.findall(text)
    for i in wordRegex.findall(text):
        for j in i:
            if j != "":
                inp_text = input(f'Enter a {j}\n')
                text = wordRegex.sub(inp_text,text,1)
    print(text)

    fileName = input("Please enter a filename\n")
    newFile = open(fileName,'w')
    newFile.write(text)
    newFile.close()
except:
    print("Enter a valid text file")
