import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index{}.html'
#url = 'https://www.ptt.cc/bbs/movie/index%s.html' (傳統寫法 可以查詢如何使用 效能較{}好)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

#1 htmp > bs4 的物件
page=9514

for i in range(0, 5):
    #爬一頁
    res = requests.get(url.format(page), headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    #2 將文章列表抓取下來 (get all title tags)
    title_tag_list = soup.select('div.title')

    for title_tag in title_tag_list:
        # print(title_tag)
        # try:
        #     title_name = title_tag.select_one('a').text #因其中有空值 所以用try except 確認問題 (因可避免>用if else)
        #     article_url = 'https://www.ptt.cc'+title_tag.select_one('a')['href']
        #     print(title_name)
        #     print(article_url)
        # except AttributeError as er:
        #     print(title_tag)
        title_name_tag = title_tag.select_one('a')
        if title_name_tag:
            title_name = title_tag.select_one('a').text
            article_url = 'https://www.ptt.cc'+title_tag.select_one('a')['href']
            print(title_name)
            print(article_url)
        else:
            print('Title is empty.')

        print('=======')

    #回上一頁
    page -= 1
