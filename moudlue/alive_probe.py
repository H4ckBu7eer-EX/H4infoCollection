import os
from datetime import datetime


def alive_probe(ip):
    dt = datetime.today()
    if ip != "":
        try:
            print("注意！使用的是ICMP探测")
            alive_probe = os.system('ping -c 1 -w 1 {}'.format(ip))

            if alive_probe:
                print('not alive!!')
            else:
                print('target alive!')
                log = open('info.h4', 'a', encoding='utf-8')
                log.write('''
Time:{}\n
Target:{}-alive'''.format(
                    ('{}:{}:{}:{}:{}'.format(dt.year, dt.month, dt.day, dt.hour, dt.minute))
                    , ip))

        except Exception as ex:
            print(ex)
    else:
        print('请输入IP!')
