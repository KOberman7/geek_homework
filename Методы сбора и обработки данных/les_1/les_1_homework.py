#1. Посмотреть документацию к API GitHub, разобраться как вывести список
#репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.
import requests
import json
from pprint import pprint
url = 'https://api.github.com'
user = 'KOberman7'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 YaBrowser/20.4.1.225 Yowser/2.5 Safari/537.36'}
info = requests.get(f'{url}/users/{user}/repos', headers=header)

with open('data.json', 'w') as f:
    json.dump(info.json(), f)

rep = []
for i in info.json():
    rep.append(i['name'])

print(f'Список репозиториев пользователя {user}: {rep}')

#2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
#Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

YOUTUBE_API_KEY= 'AIzaSyBhn3B7w3s-w5v0UuaOy8onz9GtE7RJoRI'
youtube_link = 'https://www.youtube.com/channel/UCNnZ1PMtlj1Y2Hwe-ki-gpQ?view_as=subscriber'

CHANNEL_ID = 'UCNnZ1PMtlj1Y2Hwe-ki-gpQ'


YOUTUBE_URI = 'https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults=50'
FORMAT_YOUTUBE_URI = YOUTUBE_URI.format(YOUTUBE_API_KEY, CHANNEL_ID)

content = requests.get(FORMAT_YOUTUBE_URI)
data2 = json.loads(content.text)
print(data2)

with open('data2.json', 'w') as f:
    json.dump(content.json(), f)