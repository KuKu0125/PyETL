import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/joke/index.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

res = requests.get(url, headers)
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

# print(soup)

#find用法
# logo_tag_object = soup.find('a', {'id': 'logo'})
# logo_tag_object_list = soup.findAll('a', {'id': 'logo'})
#logo_tag_object_list = soup.findAll('a', id='logo')

#select用法 find 對應到select_one (結果一樣)
logo_tag_object = soup.select_one('a[id="logo"]')
logo_tag_object_list = soup.select('a#logo')

print(logo_tag_object)
print(logo_tag_object_list)

print(logo_tag_object_list[0])
print(logo_tag_object_list[0].text)
#取超連結網址 補網域才完整
print('https://www.ptt.cc'+logo_tag_object_list[0]['href'])

print('==========')

title_tag_list = soup.select('div.title') #returns a lis of tag
print('[title_tag_list[0]]', title_tag_list[0])
print("[title_tag_list[0].find('a')]", title_tag_list[0].find('a'))
print("[title_tag_list[0].find('a').text]", title_tag_list[0].find('a').text)
print("[title_tag_list[0].find('a').[\'href\']", title_tag_list[0].find('a')['href'])

print('==========')
print(type(soup))
print(type(title_tag_list[0]))