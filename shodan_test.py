from shodan import Shodan

api = Shodan('TcUXrOqOwnqKs6fP5FpzUD8usnyuv3qv')

ipinfo = api.host('8.8.8.8')
print(ipinfo)