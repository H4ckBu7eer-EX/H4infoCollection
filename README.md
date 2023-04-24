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



更新日志
====================
4月20日更新：</br>
--------------------
dec_rpc</br>
调用：dec_rpc.dec_rpc()
</br>
原项目地址：https://github.com/Y0-kan/HostInfoScan/tree/main
</br>
app_scan </br>
调用：app_scan.app_scan(url)</br>
beian_query </br>
调用：beian_query.beian_query(url)</br>
shodanAPI配置文件</br>
