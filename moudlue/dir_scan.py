import threading

import requests
from colorama import Fore,Back,Style

def dir_scan(url,path):
    test_url=url+path
    code=requests.get(test_url).status_code
    if code ==200:
        print(f"{Fore.GREEN}[*]{Fore.WHITE}{test_url} Code:{Fore.GREEN}{code}")
    else:
        print(f"{Fore.RED}[!]{Fore.WHITE}{test_url} Code:{Fore.RED}{code}")




def read_dic(file):
    data=open(file,'r',encoding='utf-8').readlines()
    return data

def dir_scan_thread_main(url,file):
    for lines in read_dic(file):
        main_threading=threading.Thread(target=dir_scan,args=(url,lines,))
        main_threading.start()

dir_scan_thread_main('http://h4ckbu7eer.top','test_dic.txt')