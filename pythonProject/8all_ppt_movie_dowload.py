import requests
from bs4 import BeautifulSoup
#若上一頁,下一頁網址無規律 使用url=newurl

#load_article 在 load_article_test 中被定義
from load_article_test import load_article

import os

#檢查是否有某個目錄
if not os.path.exists('./articles'):
    os.mkdir('./articles')

load_folder='articles'

url = 'https://www.ptt.cc/bbs/movie/index.html'
#url = 'https://www.ptt.cc/bbs/movie/index%s.html' (傳統寫法 可以查詢如何使用 效能較{}好)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

#1 htmp > bs4 的物件


for i in range(0, 5):
    #爬一頁
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    #2 將文章列表抓取下來 (get all title tags)
    title_tag_list = soup.select('div.title')

    for title_tag in title_tag_list:

        title_name_tag = title_tag.select_one('a')
        if title_name_tag:
            title_name = title_tag.select_one('a').text
            article_url = 'https://www.ptt.cc'+title_tag.select_one('a')['href']
            """#做一隻函數儲存
            1.request article page
            2.beautifulsoup obj
            3.select article part
            4.load article text
            """
            try:
                load_article(
                    article_url=article_url,
                    load_path=f'./{load_folder}/{title_name}.txt'
                )
            except FileNotFoundError:
                load_article(
                    article_url=article_url,
                    load_path=f"./{load_folder}/{title_name.replace('/','-')}.txt",
                )
            except OSError:
                pass
            print(title_name)
            print(article_url)

        else:
            print('Title is empty.')

        print('=======')

    url = 'https://www.ptt.cc' + soup.select('a[class="btn wide"]')[1]['href']
