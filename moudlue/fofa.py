import requests
import json


def normal_query(url,email,key):
    '''普通搜索'''
    api_url = "https://fofa.info/api/v1/host/{}?email={}&key={}".format(url, email, key)
    header = {'Upgrade-Insecure-Requests': '1',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
                      }
    session=requests.session()
    rs=session.get(api_url,headers=header).text
    results=json.loads(rs)
    if 'errmsg' in results:
        if results['errmsg'] == '[40067] ErrInvalidDomain':
            print('API错误：未知域名！')
        elif results['errmsg'] == '[-700] 账号无效':
            print("API错误：账号无效！")
    else:
        return results


