import json

import requests
from scapy.all import *
from scapy.layers.inet import TCP, IP
from scapy.layers.l2 import ARP, Ether


def GetLanIpAddress(iface):
    localhost = get_if_addr(iface)
    C_Lan_Ip_Address = localhost[:(len(localhost) - localhost[::-1].find('.'))]
    return C_Lan_Ip_Address


def PublicNetPortScan(Ip_Address):
    session = requests.session()
    fofaAPI_file = open('fofaAPI3.inf', 'r', encoding='utf-8')
    fofaAPI = fofaAPI_file.readlines()
    Email = fofaAPI[1].split('=')[1].replace('\n', '')
    Key = fofaAPI[2].split('=')[1].replace('\n', '')
    print(Email)
    print(Key)
    api_url = "https://fofa.info/api/v1/host/{}?email={}&key={}".format(Ip_Address, Email, Key)
    print(api_url)
    header_windows = {'Upgrade-Insecure-Requests': '1',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
                       }
    header_linux = {}
    header_android = {}
    header_mac = {}
    headers = input("请输入需要使用的header,直接回车使用默认->\n1.Windows(默认)\n2.Linux\n3.安卓\n4.苹果\n:")
    if headers == '1' or headers == "":
        rs = session.get(api_url, verify=False, headers=header_windows)
        rs_text = rs.text
        results = json.loads(rs_text)
        ports = results['port']
        for aliveport in ports:
            print('[*]{}:{}'.format(Ip_Address, aliveport))
    if headers == '2':
        rs = session.get(api_url, verify=False, headers=header_linux)
        rs_text = rs.text
        results = json.loads(rs_text)
        ports = results['port']
        for aliveport in ports:
            print('[*]{}:{}'.format(Ip_Address, aliveport))
    if headers == '3':
        rs = session.get(api_url, verify=False, headers=header_android)
        rs_text = rs.text
        results = json.loads(rs_text)
        ports = results['port']
        for aliveport in ports:
            print('[*]{}:{}'.format(Ip_Address, aliveport))
    if headers == '4':
        rs = session.get(api_url, verify=False, headers=header_mac)
        rs_text = rs.text
        results = json.loads(rs_text)
        ports = results['port']
        for aliveport in ports:
            print('[*]{}:{}'.format(Ip_Address, aliveport))


def LanPortScan(C_Lan_Ip_Address, port):
    try:
        arp_packet = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=C_Lan_Ip_Address)
        res = srp1(arp_packet, timeout=5, verbose=False)
        if res.psrc == C_Lan_Ip_Address:
            print('[*]{}'.format(C_Lan_Ip_Address))
            try:
                pkt = IP(dst=C_Lan_Ip_Address) / TCP(dport=port, flags="S")
                response = sr1(pkt, timeout=5, verbose=False)
                if response:
                    if response.haslayer(TCP):
                        if response.getlayer(TCP).flags == 18:
                            print("[*]{}:{} Open!".format(C_Lan_Ip_Address, port))
                        else:
                            print("[!]{}:{} Close!".format(C_Lan_Ip_Address, port))
            except Exception as ex:
                print(ex)
        else:
            print('[!]{}'.format(C_Lan_Ip_Address))
    except Exception as ex:
        print(ex)


def port_scan():
    print("端口扫描")
    print('扫描本地局域网请按1，扫描外网服务器请按2')
    index = int(input(":"))
    if index == 1:
        iface = input("请输入需要扫描的无线网卡(例：eth0):")
        if iface != "":
            C_Lan_Ip = GetLanIpAddress(iface)
            for i in range(0, 65535):
                scanthreading = threading.Thread(LanPortScan(C_Lan_Ip, i))
                scanthreading.start()
    if index == 2:
        ipaddress = input("请输入需要扫描的外网IP:")
        PublicNetPortScan(ipaddress)


if __name__ == '__main__':
    port_scan()
