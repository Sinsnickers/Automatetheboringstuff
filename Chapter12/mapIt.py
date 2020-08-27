#!python3
#mapIt.py - program that opens google maps in a browser
#and takes command line arguments for search.
#if no command line argument, it uses the clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    commandLineArgument = sys.argv[1:]
    searchfor = " ".join(commandLineArgument)
else:
    searchfor = pyperclip.paste()

website = webbrowser.open("https://www.google.de/maps/place/" + searchfor)
