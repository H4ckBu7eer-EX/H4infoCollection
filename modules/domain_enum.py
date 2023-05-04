import requests
from bs4 import *
from colorama import Fore


def domain_enum(domain):
    site_str = str(domain).split('.')
    if 'www' in site_str:
        site = '.'.join(site_str[1:])
    else:
        site = domain

    Subdomain = []
    header = {'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
              }
    for i in range(1, 20):
        url = "https://cn.bing.com/search?q=site%3A" + site + "&go=Search&qs=ds&first=" + str(
            (int(i) - 1) * 10) + "&FORM=PERE"
        html = requests.get(url, stream=True, headers=header)
        sp = BeautifulSoup(html.content, 'html.parser')
        h2 = sp.findAll('h2')
        for data in h2:
            subdomain = data.a.get('href')
            if subdomain in Subdomain:
                pass
            else:
                Subdomain.append(subdomain)
                print(Fore.GREEN + '[*]' + Fore.WHITE + subdomain)
        return Subdomain
    print(len(Subdomain))


