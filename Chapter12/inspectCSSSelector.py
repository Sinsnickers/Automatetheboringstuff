import bs4

exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read(),"html.parser")
elems = exampleSoup.select("#author")
print(type(elems))
print(len(elems))
print(str(elems[0])) # The Tag object as a string.
print(elems[0].getText())
print(elems[0].attrs)
print("---------------------------------------------------------")
pElems = exampleSoup.select("p")
print(pElems[0]) #everything including selector and text of selector
print(pElems[0].getText()) #only the text of the selector
print(pElems[1])
print(pElems[1].getText())
print(pElems[2])
print(pElems[2].getText())
print("---------------------------------------------------------")
soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)
print("---------------------------------------------------------")
