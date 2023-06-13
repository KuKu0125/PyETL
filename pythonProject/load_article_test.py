import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

def load_article(article_url: str, load_path:str):
    res = requests.get(article_url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser') #變成bs4的物件
    article_tag = soup.select_one('div[id="main-content"]')#定位文章
    for tag in article_tag.select('div'): #移除全部div標籤
        tag.extract()
    #print(article_tag)

    article_content = article_tag.text #將文章儲存到 article_content
    with open(load_path, 'w', encoding = 'utf-8') as f:
        f.write(article_content)
    # print("=========")
    # article_tag.select_one('div[class="article-metaline"]').extract()#移除不要的標籤 發現全部div標籤都可刪
    # print("=========")
    # print(article_tag)
    pass


#測試這隻程式
if __name__ == '__main__':
    article_url = 'https://www.ptt.cc/bbs/movie/M.1677862363.A.7AE.html'
    load_article(article_url, "./test.txt")
