#! python3
#mcb.pyw Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")
try:
    keyWord = sys.argv[1].lower()
    if len(sys.argv)==3 and keyWord == "save":
        # TODO: Save clipboard content.
        keyWord = sys.argv[2].lower()
        text = pyperclip.paste()
        mcbShelf[keyWord] = text
    else:
        if keyWord == "list":
            pyperclip.copy(str(list(mcbShelf.keys())))
        else:
            newText = mcbShelf[keyWord]
            pyperclip.copy(newText)
            # TODO: list function has to be installed
except:
    print("Please enter valid keyword")
mcbShelf.close()