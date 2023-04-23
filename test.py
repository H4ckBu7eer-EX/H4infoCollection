import requests
from bs4 import BeautifulSoup

def google_hack(site):
    # 构造搜索链接
    url = f"https://www.google.com/search?q=site%3A{site}"
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


out=google_hack("baidu.com")
print(out)