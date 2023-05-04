import requests
import json

from style import print_green, print_red


def beian_query(url):
    # API:https://api.ooomn.com/api/icp?domain=
    try:
        api_url = f'https://api.ooomn.com/api/icp?domain={url}'
        header_windows = {"Upgrade-Insecure-Requests": '1',
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
                          }
        session = requests.session()
        requests.packages.urllib3.disable_warnings()
        re = session.get(api_url, verify=False, headers=header_windows).text
        results = json.loads(re)
        status = results['msg']
        if status == 'success':
            print_green(
                f'姓名: {results["name"]}\n域名: {results["siteindex"]}\n类型: {results["nature"]}\nICP备案: {results["icp"]}\n备案时间: {results["time"]}')
            return f'姓名: {results["name"]}\n域名: {results["siteindex"]}\n类型: {results["nature"]}\nICP备案: {results["icp"]}\n备案时间: {results["time"]}'
        else:
            print_red("[+]查询失败，可能该域名没有备案")
    except:
        print_red('[+]返回数据出错！')


def main():
    print_green('[+]当前模式为备案查询')
    print_red('退出请输入"退出/exit"')
    while True:
        url = input('请输入URL: ')
        if '退出' == url or 'exit' == url:
            break
        else:
            beian_query(url)
            print('=' * 10)


if __name__ == '__main__':
    main()
