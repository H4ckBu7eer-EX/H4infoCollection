import requests

from modules.dir_scan import dir_scan
from modules import scan_cms
from modules.github_search import github_search
from logo import *
from style import print_red, print_blue, print_green, print_white, print_yellow, print_black
from modules import beian_query, subdomain_scan, scan_js,dir_scan

# 0为内网渗透模式
# 1为外网渗透模式
modo = 1

com = '''
1.备案查询
2.子域名
3.端口扫描
4.重测平台
5.whois查询
6:dns查询
7.FOFA
8.SHODAN
9.ZOOMEYE
10.鹰眼
11.HACKING
12.github搜索
13.证书查询
14.域名枚举
15.APP扫描
16.公众号扫描
17.小程序扫描
18.PC应用程序扫描
19.IP反查域名
20.真实IP查找
21.IP注册信息查询
22.C段扫描
23.目录扫描
24.存活探测
25.敏感资产定位
26.JS信息提
27.退出
'''


def print_name1():
    functions_name = {
        "1": "备案查询",
        "2": "子域名",
        "3": "端口扫描",
        "4": "重测平台",
        "5": "whois查询",
        "6": "dns查询",
        "7": "FOFA",
        "8": "SHODAN",
        "9": "ZOOMEYE",
        "10": "鹰眼",
        "11": "搜索引擎 HACKING",
        "12": "github搜索",
        "13": "证书查询",
        "14": "域名枚举",
        "15": "APP扫描",
        "16": "公众号扫描",
        "17": "小程序扫描",
        "18": "PC应用程序扫描",
        "19": "IP反查域名",
        "20": "真实IP查找",
        "21": "IP注册信息查询",
        "22": "C段扫描",
        "23": "目录扫描",
        "24": "存活探测",
        "25": "敏感资产定位",
        "26": "JS信息提取",
        "27": "CMS指纹扫描",

    }
    print(Fore.BLUE + "==========菜单==========" + Fore.RESET)
    for key in functions_name:
        print(Fore.YELLOW + key + Fore.GREEN + ": " + functions_name[key] + Fore.RESET)


com_1 = '''
指令：
    菜单/menu  - 输出所有支持的模块
    退出/exit  - 退出工具
'''


def one_print():
    url = 'https://v1.hitokoto.cn/'
    try:
        response = requests.get(url)
        yiyantext = response.json()['hitokoto']
        print(f'{Fore.LIGHTMAGENTA_EX}=={yiyantext}=={Fore.RESET}')
    except:
        print(f'{Fore.LIGHTMAGENTA_EX}==没网你收集你妈信息呢=={Fore.RESET}')


def input_com():
    while True:
        user_input = input('请输入指令: ')
        # 退出
        if user_input == "exit" or user_input == "退出":
            print(f'{Fore.LIGHTGREEN_EX}拜拜！{Fore.RESET}')
            one_print()
            break
        # 显示这个菜单
        elif user_input == "menu" or user_input == "菜单":
            print_name1()
        # 备案查询
        elif user_input == "1":
            beian_query.main()
        # 子域名查
        elif user_input == "2":
            subdomain_scan.subdomain_scan()
        elif user_input == "3":
            print("c")
        elif user_input == "4":
            print("d")
        elif user_input == "5":
            print("e")
        elif user_input == "6":
            print("f")
        elif user_input == "7":
            print("g")
        elif user_input == "8":
            print("h")
        elif user_input == "9":
            print("i")
        elif user_input == "10":
            print("j")
        elif user_input == "11":
            print("k")
        elif user_input == "12":
            github_search()
        elif user_input == "13":
            print("m")
        elif user_input == "14":
            print("n")
        elif user_input == "15":
            print("o")
        elif user_input == "16":
            print("p")
        elif user_input == "17":
            print("q")
        elif user_input == "18":
            print("r")
        elif user_input == "19":
            print("s")
        elif user_input == "20":
            print("t")
        elif user_input == "21":
            print("u")
        elif user_input == "22":
            print("v")
        # 目录扫描
        elif user_input == "23":
            dir_scan.main()
        elif user_input == "24":
            print("x")
        elif user_input == "25":
            print("y")
        # js提取
        elif user_input == "26":
            scan_js.main()
        # cms扫描
        elif user_input == "27":
            scan_cms.main()


def main():
    logo()
    print_green(com_1)
    input_com()


if __name__ == "__main__":
    try:
        main()
    except:
        pass
