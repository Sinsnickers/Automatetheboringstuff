#! python3
# bulletPointAdder.py - Adds Wikepedia bullet pointers to the start
# of each line of the text of the clipboard

import pyperclip
text = pyperclip.paste()

#Separate lines and add stars
lines = text.split("\n")
for i in range(len(lines)): #iterate of every line of the text
    lines[i] = "* " + lines[i] #add star to the lines

text = "\n".join(lines)

pyperclip.copy(text)