import requests, bs4

# res = requests.get('http://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text)
# print(type(noStarchSoup))

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
print(type(exampleSoup))
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
auth = elems[0].getText()
print(auth)
print(str(elems[0]))
print(elems[0].attrs)

pElems = exampleSoup.select('p')
print(str(pElems[0]))

