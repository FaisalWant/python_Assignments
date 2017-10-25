import requests, os, bs4
url= 'http://xkcd.com'

os.makedirs('xkcd',exist_ok=True)

while not url.endswith('#'):
  #donwloading the page
  print('Downloading page %s...' %url)
  res= requests.get(url)
  res.raise_for_status()
  soup =bs4.BeautifulSoup(res.text)
  #find all the URL of the comic image
  comicElem= soup.select('#comic')
  if comicElem==[]:
      print('could not find comic image')
  else:
    comicUrl= comicElem[0].get('src')
    #download the image
    print ('downloading image %s...' %(comicUrl))
    res= requests.get(comicUrl)
    res.raise_for_status()

    # save the image to ./xkcd.
    imageFile= open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
    for chunk in res.iter_content(100000):
      imageFile.write(chunk)
    imageFile.close()

    #get the previous button's url.
  prevLink= soup.select('a[rel="prev"]')[0]
  url= 'http://xkcd.com'+prevLink.get('href')
print('done')
