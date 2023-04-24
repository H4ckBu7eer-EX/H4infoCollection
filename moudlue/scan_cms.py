import hashlib
import json

import requests

from H4infoCollection.style import print_green, print_red


def get_md5(url, head):
    try:
        con = requests.get(url=url, headers=head).text
        hl = hashlib.md5()
        hl.update(con.encode(encoding='utf8'))
        md5 = hl.hexdigest()
        return md5
    except:
        pass


def get_keyword(url, head):
    try:
        con = requests.get(url=url, headers=head).text
        reditList = con.history  # 可以看出获取的是一个地址序列
        print(reditList)
        if con:
            return 1
    except:
        pass


def scan_cms_finger(url, headers, json_file):
    # 加载json文件
    data = ''
    if json_file is None:
        try:
            with open('cms指纹.xml', encoding='gbk') as f:
                data = json.loads(f.read())
                # print(f.read())
        except:
            print_red('[+]cms扫描字典读取失败！')
    else:
        try:
            with open(json_file, encoding='gbk') as f:
                data = json.loads(f.read())
                # print(f.read())
        except:
            print_red('[+]cms扫描字典读取失败！')
    # https://www.yue365.com/movie/
    # 遍历所有对象和行
    # print(data['objects'][0]['rows'])
    # https://wikidiff.com/
    for obj in data['objects'][0]['rows']:
        if obj[4] == 'md5':
            md5 = get_md5(url + obj[2], headers)
            if md5 == obj[3]:
                print_green(obj[1])
                break
        if obj[4] == 'keyword':
            keyword = get_keyword(url + obj[2], headers)
            if keyword == 1:
                print_green(obj[1])
                # break

    return '检测不到'


def str_to_md5(s):
    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return m.hexdigest()


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}


def main():
    print_green('[+]当前模式为CMS指纹识别')
    print_red('退出请输入"退出/exit"')
    while True:
        url = input('请输入URL: ')
        if '退出' == url or 'exit' == url:
            break
        else:
            scan_cms_finger(url, json_file='cms指纹.xml', headers=headers)
            print('=' * 10)


if __name__ == '__main__':
    main()
