import requests
import re

api = 'http://music.taihe.com/artist'

data = {
    'key': '薛之谦'
}

# data/param区别？
req = requests.get(api, data=data)
html = req.text

# 获取歌曲id，解析网页内容
sids = re.findall(r'data-playdata="(.+?)"', html)
print(sids)
