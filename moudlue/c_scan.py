import requests
import fofa
import socket

def c_ip_get():
    session = requests.session()
    fofaAPI_file = open('./fofaAPI.inf', 'r', encoding='utf-8')
    fofaAPI = fofaAPI_file.readlines()
    Email = fofaAPI[1].split('=')[1].replace('\n', '')
    Key = fofaAPI[2].split('=')[1].replace('\n', '')
    print("C段扫描")
    url = input('请输入目标域名或者IP(例：www.baidu.com):')
    results = fofa.normal_query(url, Email, Key)
    ip = results['ip']
    ports=results['port']
    return [ip,ports]


def c_scan():
    C_IP = '.'.join(str(c_ip_get()[0]).split('.')[:3]) + '.'
    ports=c_ip_get()[1]
    print(C_IP)
    print(ports)

c_scan()
