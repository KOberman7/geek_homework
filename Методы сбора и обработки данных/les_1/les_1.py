import requests
from pprint import pprint
import json
main_link = 'https://api.openweathermap.org/data/2.5/weather'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 YaBrowser/20.4.1.225 Yowser/2.5 Safari/537.36'}
city = 'Sochi'
appid = 'd9ee9b94402050d5cd9233b3bb4055d9'
params = {'q': city,
          'appid': appid}
response = requests.get(main_link, headers=header, params=params)

if response.ok:
    data = json.loads(response.text)
pprint(data)