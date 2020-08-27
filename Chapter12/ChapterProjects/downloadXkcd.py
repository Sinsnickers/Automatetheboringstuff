#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, bs4, os

#open site per request
url = "https://xkcd.com"
os.makedirs("xkcd",exist_ok=True)
while not url.endswith('#'):
    # TODO: Download the page.
    print('Downloading page %s...' % url)
    res =requests.get(url)
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.text,"html.parser")

    # TODO: Find the URL of the comic image.
    comicElem = soup.select("#comic img")
    if comicElem == []:
        print("No comic was found")
    else:
        comicUrl = "https:" + comicElem[0].get("src")
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
print('Done.')