import requests
import json


def beian_query(url):
    # API:https://api.ooomn.com/api/icp?domain=
    print("==========备案查询==========")
    api_url = f'https://api.ooomn.com/api/icp?domain={url}'
    header_windows = {"Upgrade-Insecure-Requests": '1',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
                      }
    session = requests.session()
    re = session.get(api_url, verify=False, headers=header_windows).text
    results = json.loads(re)
    status = results['msg']
    if status == 'success':
        print(
            f'姓名：{results["name"]}\n域名:{results["siteindex"]}\n类型：{results["nature"]}\nICP备案：{results["icp"]}\n备案时间：{results["time"]}')
    else:
        print("查询失败，可能该域名没有备案")
        print(results)

