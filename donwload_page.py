#downloading a web page

import requests
res= requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))
try:
  print(res.raise_for_status())
except Exception as exc:
    print('There is a problem %s' %(exc))
playFile= open('RomeoAndJuliet.txt','wb')   #write binary mode
for chunk in res.iter_content(100000):
      playFile.write(chunk)

playFile.close()
print(res.status_code== requests.codes.ok)
print(len(res.text))
print(res.text[:250])


"""res= requests.get(\'http://inventwithpython.com/page_that_does_not\')
print(type(res))
try:
  print(res.raise_for_status())
except Exception as exc:
    print('There is a problem %s' %(exc))
"""
