import fofa
from scapy.all import *
from scapy.layers.l2 import ARP, Ether

time = datetime.now().strftime('%Y-%m-%d %H:%M')


def c_ip_get(url,email,key):
    results = fofa.normal_query(url, email, key)
    ip = results['ip']
    return ip


def c_scan_public(url,email,key):
    ip = c_ip_get(url,email,key)
    resulte = fofa.hightlevel_query(ip, email, key, 'C')
    C_ = resulte['results']
    for ips in C_:
        domain = ips[0]
        ip = ips[1]
        protocol = ''
        if ips[2] == '80':
            protocol = 'http'
            print(f'[*]Domain:{domain} IP:{ip} WebProtocol:{protocol}\n')
            return f'[*]Domain:{domain} IP:{ip} WebProtocol:{protocol}\n'
        elif ips[2] == '443':
            protocol = 'https'
            print(f'[*]Domain:{domain} IP:{ip} WebProtocol:{protocol}\n')
            return f'[*]Domain:{domain} IP:{ip} WebProtocol:{protocol}\n'


def c_scan_lan_arp(ip):
    try:
        aliveip=[]
        arp_packet = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip)
        res = srp1(arp_packet, timeout=5, verbose=False)
        if res.psrc == ip:
            print('[*]{}'.format(ip))
            aliveip.append(ip)
            return aliveip
    except:
        pass


def c_scan_lan_thread_main(ip):
    c_ip = '.'.join(str(ip).split('.')[:3]) + '.'
    for i in range(1, 256):
        start = threading.Thread(target=c_scan_lan_arp, args=(c_ip + str(i),))
        start.start()

