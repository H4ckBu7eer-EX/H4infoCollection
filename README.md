# H4infoCollection
BEST信息收集框架！
---------------------
H4IC具有强大全面的侦察，全方位多层次立体化侦察目标信息，扩展红队攻击面，发现隐藏资产与薄弱项！在编写时将所有零散脚本改变为模块调用，实现如拼装积木一般自定义自己的工具！H4infoCollection由H4ckBu7eer团队自豪地推出！


# 功能
```
1: 备案查询
2: 子域名
3: 端口扫描
4: 重测平台
5: whois查询
6: dns查询
7: FOFA
8: SHODAN
9: ZOOMEYE
10: 鹰眼
11: 搜索引擎 HACKING
12: github搜索
13: 证书查询
14: 域名枚举
15: APP扫描
16: 公众号扫描
17: 小程序扫描
18: PC应用程序扫描
19: IP反查域名
20: 真实IP查找
21: IP注册信息查询
22: C段扫描
23: 目录扫描
24: 存活探测
25: 敏感资产定位
26: JS信息提取
```

HOW TO USE?
---------------------
安装依赖: 

```
pip install -r requirements txt
```

启动框架: 

```
python run.py
```

docker启动: 

```
docker run XXXXXXXXXX
```

调用方式: 

```
import 脚本名
脚本名.功能()
```

举个例子：
```
#在你的脚本中导入目标存活检测
import alive_probe
alive_probe.alive_probe()
```


功能使用指引：
```
存活探测模块：
alive_probe.py
使用:
alive_probe.alive_probe(ip)
ip:需要检测的目标IP地址，可以是域名或者纯IP

APP查询模块：
app_scan.py
使用：
app_scan.app_scan(url,email,key)
url为需要指定查询的目标网站
email为你的fofaAPI邮箱
key为你的fofaAPIKey

备案查询模块：
beian_query.py
使用：
beian_query.beian_query(url)
url为需要指定查询的目标网站

C段扫描模块：
c_scan.py
使用：
    外网：
        c_scan.c_scan_public(url,email,key)
        url为目标网址，可以是域名和IP
        email为你的fofaAPI邮箱
        key为你的fofaAPIKey
    内网：
        c_scan.c_scan_lan_arp(ip)
        ip为你的内网IP地址

证书查询模块：
cert_query.py
使用：
cert_query.cert_query(url,email,key)
url为目标网址，可以是域名和IP
email为你的fofaAPI邮箱
key为你的fofaAPIKey

DECRPC扫描模块：
dec_rpc.py
使用：
导入模块按照指示即可

目录扫描模块：
dir_scan.py
使用：
直接导入
或
dir_scan.dir_scan_thread_main(url, file)
url为目标网址，可以是域名和IP
file为你的字典目录

DNS扫描模块：
dns_query.py
使用:
dns_query(domain,mode)
domain为目标域名
mode为你需要使用的模式，目前支持：
A,MX,NS,CNAME
模块默认为A

FOFAAPI使用模块：
fofa.py
使用：
normal_query(url,email,key)
url为目标网址，可以是域名和IP
email为你的fofaAPI邮箱
key为你的fofaAPIKey
或
hightlevel_query(url,email,key,mod)
url为目标网址，可以是域名和IP
email为你的fofaAPI邮箱
key为你的fofaAPIKey
mod为你需要使用的高级搜索模式
当前有
C：C段扫描的支持
cert:证书搜索的支持

端口扫描模块:
port_scan.py
使用：
    外网：
        PublicNetPortScan(Ip_Address, email, key)
        Ip_Address为目标Ip地址
        email为你的fofaAPI邮箱
        key为你的fofaAPIKey
    内网：
        LanPortScan(C_Lan_Ip_Address, port)
        C_Lan_Ip_Address为内网IP地址
        port为目标端口
    或：
    port_scan()根据引导即可

```