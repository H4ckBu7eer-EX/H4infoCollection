import json

import requests
from bs4 import BeautifulSoup

from style import print_green, print_red


def subdomain_scan(key):
    re = requests.get('https://www.dnsgrep.cn/subdomain/' + key)
    soup = BeautifulSoup(re.text, 'lxml')
    soup = soup.find_all('td')
    s = []
    for i in soup:
        i = i.text.replace(' ', '').replace('\n', '')
        s.append(i)
    ret = json.dumps(s, ensure_ascii=False)
    print(ret)
    return ret

def main():
    print_green('[+]当前模式为子域名查询(该模式未必包含全部数据)')
    print_red('退出请输入"退出/exit"')
    while True:
        url = input('请输入URL: ')
        if '退出' == url or 'exit' == url:
            break
        else:
            subdomain_scan(url)
            print('=' * 10)

if __name__ == '__main__':
    main()