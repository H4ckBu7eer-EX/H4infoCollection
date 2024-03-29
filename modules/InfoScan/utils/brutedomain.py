# 通过字典爆破子域名

import dns.resolver     # 判断域名是否存在的模块
from common import *
import threading
from queue import Queue     # 接收域名
import os
from urllib.parse import urlparse
import sys

class Brutedomain(object):
    # 初始化
    #q = queue.Queue()
    def __init__(self,domain,thread_count):
        self.domain = domain
        self.queue = Queue()
        self.thread_count = thread_count
        self.thread_count = int(thread_count)
        self.result = []

    def run(self):
        # 调用多线程进行爆破子域名
        print("\n[*]正在对"+self.domain+"进行子域名爆破,请稍等[*]")
        with open(os.getcwd()+'/dict/dict.txt') as f:     #载入字典
            for i in f:         # 往多线程里添加数据
                self.queue.put(i.rstrip() + '.' + self.domain)            # 拼接
        total = self.queue.qsize()  #总的数量
        threads = []

        for i in range(self.thread_count):
            threads.append(self.BruteRun(self.queue,self.result, total,self.thread_count))
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        print('\n')
        print_try("爆破完成,共爆破出" + str(len(self.result)) + "个域名\n")
        return list(set(self.result))

    class BruteRun(threading.Thread):
        def __init__(self, queue, result, total,thread_count):
            threading.Thread.__init__(self)
            self.queue = queue
            self.total = total
            self.result = result
            self.thread_count = thread_count
            self.rsv = dns.resolver.Resolver()
            #self.write = write()

        def run(self):
            #print(self.result)
            while not self.queue.empty():
                sub = self.queue.get_nowait()
                #print(sub)
                self.msg()
                try:
                    results = self.rsv.query(sub)
                    if results: 
                        for res in results:
                            if res.address != '127.0.0.1' and res.address not in self.result:
                                #print(res.address)
                                self.result.append(sub)
                                #self.write(sub)

                except Exception as e:
                    #return e
                    pass

        # 显示执行情况
        def msg(self):
            all_count = self.total
            found_count = len(list(set(self.result)))
            thread_count = self.thread_count
            use_count = self.total - self.queue.qsize()
            msg ='[*]ALL: '+str(all_count)+ ' | Thread: '+str(thread_count)+' | Schedule: '+ str(use_count)+' | Complete: '+str(round((use_count/all_count)*100,2)) +'% | Found: '+str(found_count) #+'\n' #+' [*] result: '+str(self.result)
            sys.stdout.write('\r'+str(msg))
            sys.stdout.flush()
