#!python3
#searchpypi.py - Opens several search results

import requests, sys, bs4, webbrowser
print("Searching...")  #display text while downloading the search results
res = requests.get('https://www.google.com/search?sxsrf=ALeKk03PvDNCG9h9Ylqs8NelXjqIbTEr6A%3A1598299339712&ei=yxxEX7mRK4WBhbIP7pa0-Ag&q=' + ' '.join(sys.argv[1:]))
res.raise_for_status
#Retrieve top tier search results
soup = bs4.BeautifulSoup(res.text,"html.parser")
#open a browser tab for each search result
linkElems = soup.select("div:nth-child(1) > div > div.r > div > div.TbwUpd > cite")
print(linkElems[0])
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    #print(linkElems[i])
    urlToOpen = linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)