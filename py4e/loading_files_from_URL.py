import requests

url = 'https://www.py4e.com/code3/mbox-short.txt'

r = requests.get(url, allow_redirects=True)

open('mbox-short.txt', 'wb').write(r.content)