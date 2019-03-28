#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @file     : test_random.py
# @author   : longtao
# @date     : 2019-03-28
# @version  : 1.0
# @desc     : 随机数小游戏

#导入random模块
import random

#生成随机数
s = random.randint(0, 10)

#猜数小游戏
while True:
    a = int(input("请输入一个整数： "))
    if a > s:
        print("你输入的数字较大，请再次输入。")
    elif a < s:
        print("你输入的数字过小，请再次输入。")
    else:
        print("恭喜你，你输入的数字正确。 随机数为: %d"%s)
        break