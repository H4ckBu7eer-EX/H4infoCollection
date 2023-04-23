import datetime
import fofa
from scapy.all import *
from scapy.layers.inet import TCP, IP
from scapy.layers.l2 import ARP, Ether

apifile = open('fofaAPI.inf', 'r', encoding='utf-8').read()
email = apifile.split('Email=')[1].split('Key=')[0].split('\n')[0]
key = apifile.split('Email=')[1].split('Key=')[1].split('\n')[0]
time = datetime.now().strftime('%Y-%m-%d %H:%M')


def c_ip_get(url):
    results = fofa.normal_query(url, email, key)
    ip = results['ip']
    return ip


def c_scan_public(url):
    log = open('c-scanlog_public.log', 'a', encoding='utf-8')
    ip = c_ip_get(url)
    resulte = fofa.hightlevel_query(ip, email, key, 'C')
    C_ = resulte['results']
    for ips in C_:
        domain = ips[0]
        ip = ips[1]
        protocol = ''
        if ips[2] == '80':
            protocol = 'http'
            print(f'[*]Domain:{domain} IP:{ip} WebProtocol:{protocol}\n')
            log.write(f'[*]Domain:{domain} IP:{ip} WebProtocol:{protocol} Time:{time}\n')
        elif ips[2] == '443':
            protocol = 'https'
            print(f'[*]Domain:{domain} IP:{ip} WebProtocol:{protocol}\n')
            log.write(f'[*]Domain:{domain} IP:{ip} WebProtocol:{protocol}\n')


def c_scan_lan_arp(ip):
    log = open('c-scanlog_lan.log', 'a', encoding='utf-8')
    try:
        arp_packet = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip)
        res = srp1(arp_packet, timeout=5, verbose=False)
        if res.psrc == ip:
            print('[*]{}'.format(ip))
            log.write(f'[*]{ip}\n')
    except:
        pass


def c_scan_lan_thread_main(ip):
    c_ip = '.'.join(str(ip).split('.')[:3]) + '.'
    for i in range(1, 256):
        start = threading.Thread(target=c_scan_lan_arp, args=(c_ip + str(i),))
        start.start()


c_scan_lan_thread_main('192.168.77.85')
