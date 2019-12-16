import requests

api = 'http://music.taihe.com/artist'

data = {
    'key': '薛之谦'
}

# data/param区别？
req = requests.get(api, data=data)
html = req.text

print(html)
