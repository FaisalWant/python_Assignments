import json, requests, sys
if len(sys.argv)<2:
    print('usage: quickWeather.py location')
    sys.exit()
location= ' '.join(sys.argv[1:])
# donwload the Json data from openweathermap.org's api

url= 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s' %(location)
print(type(url))
response= requests.get(url)
repsonse.raise_for_status()
#load Json data into a python variable
weatherData= json.loads(response.text)
#prin weather description
w=weatherData['list']
print('current weather is %s:' %(location))
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])
print()
print("tomorrow")
print(w[1]['weather'][0]['main'],'-',w[1]['weather'][0]['description'])
print()
print("day after tommorow")
print(w[2]['weather'][0]['main'],'-',w[2]['weather'][0]['description'])
