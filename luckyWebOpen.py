#! /usr/bin/env python3

import requests, sys, webbrowser, bs4

print('Googling...')  # display text while downloading the Google Page
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

print(res)
# to do retrieve top search result links
soup = bs4.BeautifulSoup(res.text, features="html.parser")

print(soup)

# to do open a browser tab for each result
linkElems = soup.select('.r a')
print(linkElems)

numOpen = min(5, len(linkElems))

for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))


