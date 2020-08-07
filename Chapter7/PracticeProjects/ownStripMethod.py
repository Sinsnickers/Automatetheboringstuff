#! python3
import re

def strippy(text,argument=""):
    if argument == "":
        stripRegex = re.compile(r"\s*(\w)\s*")
        strippy = stripRegex.sub(r"\1",text)
    else:
        arguments ="["+argument+"]*"
        stripRegex = re.compile(arguments)
        strippy = stripRegex.sub("",text)
    return strippy

text = ",,,,,rrttgg.....banana....rrr"
text2 = "               banana2           "
output = strippy(text,".,rgt")
output2 = strippy(text2)
print(output)
print(output2)

