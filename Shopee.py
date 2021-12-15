import requests
import parsel
import re
import pprint
from concurrent.futures import ThreadPoolExecutor
def parse(url):
    resp=requests.get(url=url,headers=headers)
    # pprint.pprint(resp.json())
    name=resp.json()['items']#['item_basic']['name']
    for x in range(len(name)):
        print(name[x]['item_basic']['name'])
if __name__ =='__main__':
    # kw=input('what do you want to search: ')
    with ThreadPoolExecutor(20) as t:
        for x in range(15):
            url = f'https://shopee.com.my/api/v4/search/search_items?by=relevancy&keyword=python&limit=60&newest={x * 60}&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
            }
            t.submit(parse,url)
