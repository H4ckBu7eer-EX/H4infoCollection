import requests
import json
import base64

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

def hightlevel_query(url,email,key,mod):
    #https://fofa.info/api/v1/search/all?email=your_email&key=your_key&qbase64=dGl0bGU9ImJpbmci
    #ip="103.74.192.2/24"
    session=requests.session()
    #C段
    if mod == "C":
        query_word=f'ip="{url}/24"'
        qbase64=base64.b64encode(query_word.encode('utf-8'))
        header = {'Upgrade-Insecure-Requests': '1',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
                  }
        api_url=f"https://fofa.info/api/v1/search/all?email={email}&key={key}&qbase64={qbase64.decode()}"
        rs=session.get(api_url,headers=header).text
        results = json.loads(rs)
        return results
    #证书查询
    if mod == "cert":
        query_word=f'cert="{url}"'
        qbase64 = base64.b64encode(query_word.encode('utf-8'))
        header = {'Upgrade-Insecure-Requests': '1',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
                  }
        api_url = f"https://fofa.info/api/v1/search/all?email={email}&key={key}&qbase64={qbase64.decode()}"
        rs = session.get(api_url, headers=header).text
        results = json.loads(rs)
        return results
