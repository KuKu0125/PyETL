import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index9514.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

#1 htmp > bs4 的物件
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

#2 將文章列表抓取下來 (get all title tags)
title_tag_list = soup.select('div.title')

for title_tag in title_tag_list:
    # print(title_tag)
    title_name = title_tag.select_one('a').text
    article_url = 'https://www.ptt.cc'+title_tag.select_one('a')['href']
    print(title_name)
    print(article_url)
    print('=======')
