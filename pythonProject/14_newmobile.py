import pprint

import requests
from bs4 import BeautifulSoup

url ='https://www.newmobilelife.com/wp-json/csco/v1/more-posts'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

data_str = """action: csco_ajax_load_more
page: 2
posts_per_page: 30"""

data = {row.split(':')[0]: row.split(':')[1] for row in data_str.split('\n')}
#print(data)

res = requests.post(url, headers=headers, data=data)
json_data = res.json()
"""{'data': {'content': '\n'
                     '\n'
                     '<article class="post-482716 post type-post '
                     'status-publish format-standard has-post-thumbnail '"""
html_str = json_data['data']['content'] #html的字串
soup = BeautifulSoup(html_str, 'html.parser')
#pprint.pprint(json_data)
for title_obj in soup.select('h2[class="cs-entry__title"]'):
    print(title_obj)
    print('======')