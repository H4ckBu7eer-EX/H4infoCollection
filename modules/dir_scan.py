import threading

import requests
from colorama import Fore, Back, Style

from style import print_green,print_red


def dir_scan(url, path: str):
    if (not path == '') or (not path is None):
        path = path.replace('\n', '')
    test_url = url + path
    pathlist=[]
    try:
        code = requests.get(test_url)
        if code.status_code == 200:
            print(f"{Fore.GREEN}[+][{len(code.text)}]{Fore.WHITE}{test_url} Code:{Fore.GREEN}{code.status_code}{Fore.RESET}")
            pathlist.append(test_url+' Code:'+code.status_code)
        elif code == 403:
            print(f"{Fore.YELLOW}[!][{len(code.text)}]{Fore.WHITE}{test_url} Code:{Fore.YELLOW}{code.status_code}{Fore.RESET}")
            pathlist.append(test_url + ' Code:' + code.status_code)
        elif code == 302:
            print(f"{Fore.YELLOW}[!][{len(code.text)}]{Fore.WHITE}{test_url} Code:{Fore.YELLOW}{code.status_code}{Fore.RESET}")
            pathlist.append(test_url + ' Code:' + code.status_code)
    except:
        pass


def read_dic(file):
    data = open(file, 'r', encoding='utf-8').readlines()
    return data


def dir_scan_thread_main(url, file='test_dic.txt'):
    for lines in read_dic(file):
        main_threading = threading.Thread(target=dir_scan, args=(url, lines,))
        main_threading.start()
        main_threading.join()


# 'http://baidu.com','test_dic.txt'
def main():
    print_green('[+]当前模式为路径扫描')
    print_red('退出请输入"退出/exit"')
    while True:
        url = input('请输入URL: ')
        if (url == '') or (url is None):
            print_red('[!]没输入url你扫你妈呢？')
        else:
            file = input('请输入字典目录(默认使用工具预设字典): ')
            if '退出' == url or 'exit' == url:
                break
            else:
                if file is None or file == '':
                    dir_scan_thread_main(url)
                    print('=' * 10)
                else:
                    dir_scan_thread_main(url, file)
                    print('=' * 10)


if __name__ == '__main__':
    main()
