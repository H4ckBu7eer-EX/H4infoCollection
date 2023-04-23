import fofa


apifile = open('fofaAPI.inf', 'r', encoding='utf-8').read()
email = apifile.split('Email=')[1].split('Key=')[0].split('\n')[0]
key = apifile.split('Email=')[1].split('Key=')[1].split('\n')[0]
def cert_query(url):
    log=open('certlog.log','a',encoding='utf-8')
    print('同证书域名：')
    results=fofa.hightlevel_query(url,email,key,'cert')
    web_message_results=results['results']
    for web in web_message_results:
        web_domain_ip=web[0]
        origin_ip=web[1]
        print(f'[*]域名：{web_domain_ip} IP：{origin_ip} 证书：{url}')
        log.write(f'[*]域名：{web_domain_ip} IP：{origin_ip} 证书：{url}\n')

cert_query('baidu')