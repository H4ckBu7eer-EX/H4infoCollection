import requests
from bs4 import BeautifulSoup

def google_hack(site,num,payload):
    # 构造搜索链接
    url = f"https://search.modalogi.com/search?q=site:{site}%20AND%20{payload}&pageno={num}"
    # 添加请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    # 发送请求
    response = requests.get(url, headers=headers)
    # 解析响应
    soup = BeautifulSoup(response.text, "html.parser")
    # 获取所有的搜索结果
    search_results = soup.find_all("div", class_="g")
    # 提取每个搜索结果的网址
    urls = [result.find("a")["href"] for result in search_results]
    # 返回所有的网址
    return urls



def baidu_hack(site,num,payload):
    rnum=(num-1)*10   # 构造搜索链接
    url = f"https://www.baidu.com/s?ie=utf-8&wd=site:{site}%20AND%20{payload}&pn={rnum}"
    print(url)
    # 添加请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    # 发送请求
    response = requests.get(url, headers=headers)
    # 解析响应
    soup = BeautifulSoup(response.text, "html.parser")
    # 获取所有的搜索结果
    search_results = soup.find_all("div", class_="result c-container ")
    # 提取每个搜索结果的网址
    urls = [result.find("a")["href"] for result in search_results]
    print(urls)
    # 返回所有的网址
    return urls

# 调用函数并输出结果
#out = baidu_hack("baidu.com")
#print(out)


#out=google_hack("baidu.com")
#print(out)

# Create a dictionary with the specified search queries
search_dict = {
    "intitle:登录": "",
    "intitle:后台": "",
    "intitle:管理": "",
    "intitle:admin": "",
    "intitle:manage": "",
    "intitle:API": "",
    "inurl:admin": "",
    "inurl:file": "",
    "inurl:upload": "",
    "inurl:download": "",
    "inurl:api": "",
    "inurl:login": "",
    "inurl:manage": "",
    "inurl:readme": "",
    "inurl:log": "",
    "inurl:config": "",
    "inurl:cfg": "",
    "inurl:doc": "",
    "inurl:document": "",
    "inurl:cmd": "",
    "index of /admin": "",
    "index of /passwd": "",
    "index of /password": "",
    "index of /mail": "",
    "index of /\"+passwd": "",
    "index of /\"+password.txt": "",
    "index of /\"+.htaccess": "",
    "index of /root": "",
    "index of /cgi-bin": "",
    "index of /logs": "",
    "index of /config": "",
    "filetype:txt": "",
    "filetype:doc": "",
    "filetype:md": "",
    "filetype:xml": "",
    "filetype:zip": "",
    "filetype:rar": "",
    "filetype:xlsx": "",
    "filetype:xls": ""
}


search_list = list(search_dict.keys())

print(search_list)

for rpayload in search_list:
    for num in range(1,4):
        baidu_hack("bilibili.com",num,rpayload)