import requests

send_headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'BAIDUID=BBC3B3F2461D8932E653C3EC6B8107F6:FG=1; tracesrc=-1%7C%7C-1; u_lo=0; u_id=; u_t=; app_vip=show; Hm_lvt_d0ad46e4afeacf34cd12de4c9b553aa6=1577492079,1577497069,1577584707; __qianqian_pop_tt=5; log_sid=1577605543657BBC3B3F2461D8932E653C3EC6B8107F6; Hm_lpvt_d0ad46e4afeacf34cd12de4c9b553aa6=1577605992',
    'Host': 'music.taihe.com',
    'Referer': 'http://music.taihe.com/artist/1557',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}  # 伪装成浏览器
response = requests.get('http://music.taihe.com/data/user/getsongs?start=15&size=15&ting_uid=164528737', headers=send_headers)
print(response.text)
