import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from H4infoCollection.style import print_red, print_green



def search(con):
    search_url = f'https://weixin.sogou.com/weixin?type=2&s_from=input&ie=utf8&query={con}'
    wb = webdriver.Chrome()
    wb.get(search_url)

    print(wb.page_source)
    soup = BeautifulSoup(wb.page_source, 'html.parser')
    txt_box = soup.find('div', class_='txt-box')

    title = txt_box.h3.a.text
    author = txt_box.find('a', class_='account').text
    time = txt_box.find('span', class_='s2').text
    summary = txt_box.find('p', class_='txt-info').text
    content = txt_box.find('div', class_='s-p').text

    print('标题:', title)
    print('作者:', author)
    print('时间:', time)
    print('概要:', summary)
    print('全文:', content)

def main():
    print_green('[+]当前模式为公众号扫描')
    print_red('退出请输入"退出/exit"')
    while True:
        url = input('请输入内容: ')
        if '退出' == url or 'exit' == url:
            break
        else:
            search('')
            print('=' * 10)


if __name__ == '__main__':
    main()

