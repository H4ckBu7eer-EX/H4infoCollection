import requests
import json
import ssl
import os
import sys
import tableprint as tp

def get_req(search_type, data):
    url = f"https://zhishuapi.aldwx.com/Main/action/{search_type}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        "Accept": "text/html, application/xhtml+xml, image/jxr, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://www.aldzs.com",
    }
    response = requests.post(url, headers=headers, data=data, verify=False)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        sys.exit(1)
    return json.loads(response.text)["data"]

def get_info_by_keyword(options):
    ens_infos = {}
    ens_out_map = {}

    keyword = options["KeyWord"]
    # Get token information
    token = options["CookieInfo"]
    print(f"Querying for keyword '{keyword}'")
    app_list = get_req("Search/Search/search", {
        "appName": keyword,
        "page": "1",
        "token": token,
        "visit_type": "1",
    })
    if len(app_list) == 0:
        return
    tp.table(app_list, headers=["NO", "ID", "小程序名称", "所属公司", "描述"])
    # Default to the first app for querying
    print(f"Querying for apps developed by {app_list[0]['company']} (defaulting to first app)")
    app_key = app_list[0]["appKey"]
    s_app_list = get_req("Miniapp/App/sameBodyAppList", {
        "appKey": app_key,
        "page": "1",
        "size": "100",
        "token": token,
    })
    ens_infos["wx_app"] = s_app_list
    tp.table(s_app_list, headers=["NO", "ID", "小程序名称", "描述"])

    ens_out_map = {
        "wx_app": {
            "Name": "微信小程序",
            "Field": ["name", "categoryTitle", "logo", "", "", "inFrom"],
            "KeyWord": ["名称", "分类", "头像", "二维码", "阅读量", "数据关联"],
        },
    }
    return ens_infos, ens_out_map
