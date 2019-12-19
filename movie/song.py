# encoding:utf-8
import requests
import re
from bs4 import BeautifulSoup

api = 'http://music.taihe.com/search'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

data = {
    'key': '演员'
}

# data/param区别？
req = requests.get(api, params=data, headers=header)
req.encoding = req.apparent_encoding
# print(html)
# 获取歌曲id，解析网页内容
soup = BeautifulSoup(req.text, 'html.parser')
print(soup.prettify())
print(soup.find_all('a'))
