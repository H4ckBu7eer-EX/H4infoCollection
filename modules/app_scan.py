import fofa
from colorama import Fore


def app_scan(url, email, key):
    print("==========APP查询==========")
    results = fofa.normal_query(url, email, key)
    product = results['product']
    for products in product:
        print(Fore.GREEN + '[*]' + Fore.WHITE + products)
    return product
