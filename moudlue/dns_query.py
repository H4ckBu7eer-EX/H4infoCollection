import dns.resolver
from colorama import Fore
import datetime


def dns_query(domain, mode='A'):
    mode_list = ['A', 'MX', 'NS', 'CNAME']
    if mode in mode_list:
        answers = dns.resolver.resolve(domain, mode)
        for data in answers:
            print(Fore.GREEN + '[*]' + Fore.WHITE + str(data) + ' ' + mode)
            dns_log('[*]' + str(data) + ' ' + mode + '\n')
    else:
        print('你输入了一个不支持的模式！')


def dns_log(line):
    time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')
    file = open('dnslog.log', 'a', encoding='utf-8')
    log_data = \
        f'''
========-----DNS 查询日志-----==========
Time: {time} 
                '''
    file.write(log_data + line)
