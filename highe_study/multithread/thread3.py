#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @file     : thread3.py
# @author   : longtao
# @date     : 2019-04-03   
# @des      : 多线程的锁定与解锁

#导入模块
import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开启线程" + self.name)
        #获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        #释放锁
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s; %s" %(threadName, time.ctime(time.time())))
        counter -= 1

#获取锁
threadLock = threading.Lock()
threads = []

#创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

#开启新的线程
thread1.start()
thread2.start()

#添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

#等待所有的线程完成
for t in threads:
    t.join()
print("退出线程")