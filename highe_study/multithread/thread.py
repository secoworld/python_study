#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @file     : thread.py
# @author   : longtao
# @date     : 2019-04-03
# @des      : 多线程

#导入函数
import _thread
import time

#为线程创建一个新的函数
def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s, %s" %(thread_name, time.ctime(time.time())))

#创建2个线程
try:
    _thread.start_new_thread(print_time, ("thread - 1 :", 1))
    _thread.start_new_thread(print_time, ("thread - 2 :", 2))
except:
    print("Error:无法启动线程")

while 1:
    pass