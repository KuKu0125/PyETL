import requests

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

ss = requests.session()
ss.cookies['over18'] = '1' #讓ppt知道還在連線 cookies在這次連線都會被保存 之後發出的請求都會帶上
print(ss.cookiew)
res = ss.get(url, headers=headers)

print(res.text)