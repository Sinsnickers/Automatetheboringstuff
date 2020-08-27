#!python3
#linkverification.py - opens given email address and 
#try to open every link on this, mark 404 pages as broken links

import sys, bs4, requests, webbrowser

url = ("https://automatetheboringstuff.com/2e/chapter12/")
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
elems = soup.findAll("a",href=True)
for elem in elems:
    if "https:" in elem["href"]:
        link = requests.get(elem["href"])
        #link.raise_for_status()
        print(link.status_code)
#print(len(elems))
