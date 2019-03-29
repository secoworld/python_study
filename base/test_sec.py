#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @file     : test_sec.py
# @author   : longtao
# @date     : 2019-03-29
# @version  : 1.0 
# @desc     : 计时

import time
print("按下回车计时开始, 按下Ctrl + C 结束计时。")
while True:
    try:
        input()
        starttime = time.time()
        print("开始")
        while True:
            print("计时：", round(time.time() - starttime, 0), end='\r')
            time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        endtime = time.time()
        print('总共时间为：', round(time.time() - starttime, 0), 'secs')
        break
