import dns.resolver
from colorama import Fore
import datetime


def dns_query(domain, mode='A'):
    mode_list = ['A', 'MX', 'NS', 'CNAME']
    if mode in mode_list:
        answers = dns.resolver.resolve(domain, mode)
        for data in answers:
            print(Fore.GREEN + '[*]' + Fore.WHITE + str(data) + ' ' + mode)
            return data+' '+mode
    else:
        print('你输入了一个不支持的模式！')



