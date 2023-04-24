import requests

from moudlue import scan_cms
from moudlue.github_search import github_search
from logo import *
from style import print_red, print_blue, print_green, print_white, print_yellow, print_black
from moudlue import beian_query, subdomain_scan, scan_js

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


# def hostin():
#     target = input("输入目标: ")
#     with open("host.txt", "w") as f:
#         f.write(target)
#         f.close


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


# def print_name2():
#     functions_name = {
#         "1": "Aopo",
#         "2": "SbScan",
#         "3": "DCERPC",
#         "4": "otherTools",
#         "5": "otherTools",
#         "6": "返回全部菜单",
#         "7": "退出工具",
#     }
#     print(Fore.BLUE + "==========菜单==========" + Fore.RESET)
#     for key in functions_name:
#         print(Fore.YELLOW + key + Fore.GREEN + ": " + functions_name[key] + Fore.RESET)


# '''
# func_dict = {
#     "1": beian_query,
#     "2": subdomain_scan,
#     "3": port_scan,
#     "4": retest_platform,
#     "5": whois_query,
#     "6": dns_query,
#     "7": fofa,
#     "8": shodan,
#     "9": zoomeye,
#     "10": eagle_eye,
#     "11": google_hacking,
#     "12": github_search,
#     "13": cert_query,
#     "14": domain_enum,
#     "15": app_scan,
#     "16": wechat_scan,
#     "17": mini_program_scan,
#     "18": pc_app_scan,
#     "19": ip_to_domain,
#     "20": real_ip_lookup,
#     "21": ip_reg_query,
#     "22": c_scan,
#     "23": dir_scan,
#     "24": alive_probe,
#     "25": sensitive_asset_locate
# }
# '''


# def extranet():
#     while True:
#         print_name1()
#         user_input = input("选择数字,exit=>退出,menu=>菜单: ")


# def intranet():
#     while True:
#         print_name2()
#         user_input = input("请输入指令: ")
#         if user_input == "exit":
#             break
#         elif user_input == "menu":
#             print_name2()
#         elif user_input == "1":
#             print("Aopo")
#         elif user_input == "2":
#             print("SbScan")
#         elif user_input == "3":
#             print("Other")
#         elif user_input == "4":
#             print("Other")
#         elif user_input == "5":
#             print("Other")
#         elif user_input == "6":
#             break
#         elif user_input == "7":
#             print("Other")


# def mode():
#     print("1.内网渗透\n2.外网渗透")
#     selcet = int(input("模式选择："))
#     if selcet == 1:
#         intranet()
#     elif selcet == 2:
#         extranet()


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
            beian_query.beian_query()
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
            print("l")
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
        elif user_input == "23":
            print("w")
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
