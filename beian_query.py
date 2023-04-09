import webbrowser

def beian_query():
    print("==========备案查询==========")
    url_input = input("输入查询的相关信息: ")
    print("==========天眼查==========")
    url = f"https://www.tianyancha.com/search?key={url_input}"
    webbrowser.open(url)
    print("==========爱企查==========")
    url = f"https://aiqicha.baidu.com/s?q={url_input}"
    webbrowser.open(url)
    print("==========企查查==========")
    url = f"https://www.qcc.com/web/search?key={url_input}"
    webbrowser.open(url)

