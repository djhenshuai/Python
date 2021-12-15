import requests
import re
import parsel
import pprint
import csv
from concurrent.futures import ThreadPoolExecutor
import json

def main(url,headers,csv_writer):
    resp=requests.get(url=url,headers=headers)
    # print(resp.text)
    info=re.findall('window.__SEARCH_RESULT__ = (.*?)</script>',resp.text)[0]
    info=json.loads(info)['engine_jds']
    for index in info:
        dit={
            '岗位名称':index['job_name'],
            '公司名称':index['company_name'],
            '公司类型':index['companytype_text'],
            '公司规模': index['companysize_text'],
            '地点':index['workarea_text'],
            '学历':index['attribute_text'][2],
            '工作经验':index['attribute_text'][1],
            '工资':index['providesalary_text'],
        }

        csv_writer.writerow(dit)
        print(dit.values())

def parse():
    f=open('51job.csv',mode='a',encoding='utf-8',newline='')
    csv_writer=csv.DictWriter(f,fieldnames=[
        '岗位名称',
        '公司名称',
        '公司类型',
        '公司规模',
        '地点',
        '学历',
        '工作经验',
        '工资',
    ])
    csv_writer.writeheader()
    with ThreadPoolExecutor(20) as t:
        for x in range(2):
            url=f'https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,{x}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
                        }
            t.submit(main,url,headers,csv_writer)
parse()

