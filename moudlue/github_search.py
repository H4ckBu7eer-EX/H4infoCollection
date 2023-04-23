import requests


def github_search():
    # print("github搜索")
    # https: // api.github.com / search / repositories?q =
    requests.get('https://api.github.com/search/repositories?q=')