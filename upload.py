 
def upload(version):
    import requests
    print("当前版本为V"+str(version))
    print("检查更新中...")
    url = "https://h4ckbu7eer-ex.github.io/H4ckBu7eer-EX/upload.html"
    response = requests.get(url)
    if response.status_code == 200:
        print("最新版本为V"+str(int(response.text)))
        if int(response.text) <= version:
            print("已经是最新版本")
        else:
            print("软件非最新版本，请前往github更新")
    else:
        print("请求失败...")


upload(0.5)