import requests
import fofa
import socket

apifile = open('fofaAPI.inf', 'r', encoding='utf-8').read()
email = apifile.split('Email=')[1].split('Key=')[0].split('\n')[0]
key = apifile.split('Email=')[1].split('Key=')[1].split('\n')[0]
def c_ip_get(url):
    results = fofa.normal_query(url, email, key)
    ip = results['ip']
    return ip


def c_scan(url):
    log=open('c-scanlog.log','a',encoding='utf-8')
    ip=c_ip_get(url)
    resulte=fofa.hightlevel_query(ip,email,key,'C')
    C_=resulte['results']
    for ips in C_:
        domain=ips[0]
        ip=ips[1]
        protocol=''
        if ips[2] =='80':
            protocol='http'
            print(f'[*]Domain:{domain} IP:{ip} WebProtocol:{protocol}\n')
            log.write(f'[*]Domain:{domain} IP:{ip} WebProtocol:{protocol}\n')
        elif ips[2] =='443':
            protocol ='https'
            print(f'[*]Domain:{domain} IP:{ip} WebProtocol:{protocol}\n')
            log.write(f'[*]Domain:{domain} IP:{ip} WebProtocol:{protocol}\n')



print(c_scan('www.baidu.com'))