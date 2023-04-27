import os
import subprocess
from datetime import datetime

from H4infoCollection.style import print_green, print_red


def get_alive_probe(ip=None):
    dt = datetime.today()
    if (ip != "") or (not ip is None):
        try:
            # alive_probe = os.system('ping -c 1 -w 1 {}'.format(ip))
            alive_probe = subprocess.run(["ping", "-c", "1", "-w", "1", "{}".format(ip)])
            if alive_probe:
                print_red('[+]啥也没有！')
            else:
                print_green('[+]扫描完成')
                log = open('info.h4', 'a', encoding='utf-8')
                log.write('''
Time:{}\n
Target:{}-alive'''.format(
                    ('{}:{}:{}:{}:{}'.format(dt.year, dt.month, dt.day, dt.hour, dt.minute))
                    , ip))

        except Exception as ex:
            print(ex)
    else:
        return


def main():
    print_green('[+]当前模式为ICMP扫描')
    print_red('退出请输入"退出/exit"')
    while True:
        url = input('请输入IP: ')
        if '退出' == url or 'exit' == url:
            break
        else:
            get_alive_probe(url)
            print('=' * 10)


if __name__ == '__main__':
    main()
