from colorama import Fore
from scapy.layers.inet import ICMP, TCP, UDP, IP, sr1


def scan_icmp(ip):
    packet = IP(dst=ip) / ICMP()
    ans = sr1(packet, timeout=0.5, verbose=0)
    if ans:
        print('    ' + Fore.GREEN + '[*]' + Fore.WHITE + ip + ' ICMP Online')
        return 'online'
    else:
        print('    ' + Fore.RED + '[!]' + Fore.WHITE + ip + ' ICMP Lost')
        return 'offline'


def scan_tcp(ip):
    packet = IP(dst=ip) / TCP()
    ans = sr1(packet, timeout=5, verbose=0)
    if ans:
        if ans.getlayer(TCP).flags == 'SA':
            print('    ' + Fore.GREEN + "[*]" + Fore.WHITE + ip + " TCP Open")
            return 'SA'
        if ans.getlayer(TCP).flags == 'RA':
            print('    ' + Fore.YELLOW + "[!]" + Fore.WHITE + ip + " TCP Lost")
            return 'RA'


def scan_udp(ip):
    """
    注意！！！！！！
    UDP只能用于扫描内网！！！！！
    """
    packet = IP(dst=ip) / UDP(dport=56789)
    result = sr1(packet, timeout=0.5, verbose=0)
    if int(result[IP].proto) == 0x01:
        print('    ' + Fore.GREEN + '[*]' + Fore.WHITE + ip + ' UDP Online')
        return 'online'
    else:
        print('    ' + Fore.RED + '[!]' + Fore.RED + ip + ' UDP Lost')
        return 'offline'


def alive_prove(ip, mod):
    if mod == 'offline':
        print(Fore.YELLOW + '模式：离线 ' + Fore.GREEN + ip + Fore.RESET + ' -->>')
        icmp, tcp, udp = scan_icmp(ip), scan_tcp(ip), scan_udp(ip)
        return [icmp, tcp, udp]
    if mod == 'online':
        print(Fore.BLUE + '模式：在线 ' + Fore.GREEN + ip + Fore.RESET + ' -->>')
        icmp = scan_icmp(ip)
        tcp = scan_tcp(ip)
        return [icmp,tcp]




