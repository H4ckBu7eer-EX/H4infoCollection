from shodan import Shodan


def shodan_search(apikey,host):
    key=apikey
    shodan_api=Shodan(key)
    for info in shodan_api.host(host).items():
        print(info)



#api = Shodan('TcUXrOqOwnqKs6fP5FpzUD8usnyuv3qv')

shodan_search('TcUXrOqOwnqKs6fP5FpzUD8usnyuv3qv','8.8.8.8')