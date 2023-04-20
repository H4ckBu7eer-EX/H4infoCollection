import requests
import json
def app_scan(url):
    print("==========APP查询==========")
    session = requests.session()
    fofaAPI_file = open('./fofaAPI.inf', 'r', encoding='utf-8')
    fofaAPI = fofaAPI_file.readlines()
    Email = fofaAPI[1].split('=')[1].replace('\n', '')
    Key = fofaAPI[2].split('=')[1].replace('\n', '')
    print(Email)
    print(Key)
    api_url = "https://fofa.info/api/v1/host/{}?email={}&key={}".format(url, Email, Key)
    print(api_url)
    header_windows = {'Upgrade-Insecure-Requests': '1',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
                      }
    header_linux = {}
    header_android = {}
    header_mac = {}
    headers = input("请输入需要使用的header,直接回车使用默认->\n1.Windows(默认)\n2.Linux\n3.安卓\n4.苹果\n:")
    if headers == '1' or headers == "":
        rs = session.get(api_url, verify=False, headers=header_windows)
        rs_text = rs.text
        results = json.loads(rs_text)
        product = results['product']
        for products in product:
            print('[*]'+products)
