import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(type(res))
res.raise_for_status()
print(res.status_code == requests.codes.ok) #tells if the status was ok
print(len(res.text)) #gives the length of the imported text
print(res.text[:500])

#res2 = requests.get("https://inventwithpython.com/thatLinkDoesntExist.txt") #this link is a false link
#print(type(res2))
#print(res2.status_code == requests.codes.ok) #tells if the status was ok
#res2.raise_for_status() #this will raise an error if the page was false, crashes the prog on purpose

#save the downloaded text to a file 

playFile = open("c:\\users\\bero8\\boringstuff\\automatetheboringstuff\\Chapter12\\RomeoAndJuliet.txt","wb") #wb is important cause its for write binary!
for chunk in res.iter_content(100000):
        playFile.write(chunk)
playFile.close()