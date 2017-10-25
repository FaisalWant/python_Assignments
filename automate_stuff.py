import requests, bs4
res= open('examplefile.html')
#res.raise_for_status()
noStrachSoup= bs4.BeautifulSoup(res.read())
print(type(noStrachSoup))
#print(noStrachSoup)
elems= noStrachSoup.select('#author')
"""print(type(elems))
print(len(elems))
for i in range(len(elems)):
 #print(type(elems[i]))
 print(elems[i].getText())
 print(str(elems[i]))
 print(elems[i].attrs)


print(noStrachSoup.select('div'))
print(noStrachSoup.select('#author'))
print(noStrachSoup.select('p'))
print(noStrachSoup.select('div span'))
print(noStrachSoup.select('div > span'))
print(noStrachSoup.select('input[name]'))
print(noStrachSoup.select('input[type="button"]'))


pelems= noStrachSoup.select('p')
print(pelems[0])
print(len(pelems))
print(pelems[0].getText()) #returnss the  value enclosed in the angular brackets
print(str(pelems[1]))
print(pelems[1].getText())
print(str(pelems[2]))
print(pelems[2].getText())
"""

# getting data from an element's attributes

spanElem=noStrachSoup.select('span')[2]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr')==None)
print(spanElem.attrs)
