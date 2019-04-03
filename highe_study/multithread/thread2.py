#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @file     : thread2.py
# @author   : longtao
# @date     : 2019-04-03
# @des      : 多线程使用threading模块

#导入模块
import threading 
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" %(threadName, time.ctime(time.time())))
        counter -= 1

#创建新的线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

#开启新的线程
thread1.start()         #star()开始启用线程，调用myThread类中的run()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")