import requests

from style import print_green, print_red


def github_search(q):
    # print("github搜索")
    # https: // api.github.com / search / repositories?q =
    try:
        con = requests.get(f'https://api.github.com/search/repositories?q={q}').text
        print(con)
        return con
    except TimeoutError:
        print_red('[+]已超时！请优化网络')
    except Exception as e:
        print_red(f'[+]连接失败，错误信息:{e}')

mune = '''1.简单搜索(返回粗略数据)
2.详细搜索(返回详细数据，数据量过大)
3.退出/exit(退出当前模式)
'''

def main():
    # print_green('[+]当前模式为github搜索')
    print_green(mune)
    while True:
        url = input('请输入URL: ')
        if '退出' == url or 'exit' == url:
            break
        else:
            github_search(url)
            print('=' * 10)


if __name__ == '__main__':
    main()
