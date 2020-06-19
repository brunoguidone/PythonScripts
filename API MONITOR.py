import requests

URL = ''
HEADERS = {'Authorization': ''}

r = requests.get(URL, headers=HEADERS)


print(r.status_code)