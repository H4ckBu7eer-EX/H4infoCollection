from scapy.all import *
from scapy.layers.inet import TCP, IP
from scapy.layers.l2 import ARP, Ether
import fofa
from colorama import Fore

def GetLanIpAddress(iface):
    localhost = get_if_addr(iface)
    C_Lan_Ip_Address = localhost[:(len(localhost) - localhost[::-1].find('.'))]
    return C_Lan_Ip_Address


def PublicNetPortScan(Ip_Address, email, key):
    results = fofa.normal_query(Ip_Address, email, key)
    ports = results['port']
    for aliveport in ports:
        print(f'{Fore.GREEN}[*]{Fore.WHITE}{Ip_Address}:{aliveport}')


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
                            print(f"{Fore.GREEN}[*]{Fore.WHITE}{C_Lan_Ip_Address}:{ port} Open!")
                        else:
                            print(f"{Fore.RED}[!]{Fore.WHITE}{C_Lan_Ip_Address}:{port} Close!")
            except Exception as ex:
                print(ex)
        else:
            print('[!]{}'.format(C_Lan_Ip_Address))
    except Exception as ex:
        print(ex)


def port_scan():
    print("==========端口扫描==========")
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
        email=input('请输入你的FOFAAPI邮箱：')
        key=input('请输入你的FOFAAPIKey：')
        PublicNetPortScan(ipaddress,email,key)
