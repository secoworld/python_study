#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @file     : test_factorial.py
# @author   : longtao
# @date     : 2019-03-29
# @version  : 1.0
# @desc     : 整数的阶乘

#用户输入数字
num = int(input("请输入一个数字："))
factorial = 1

#查看数字是正数还是负数
if num < 0:
    print("抱歉，负数没有阶乘.")
elif num == 0:
    print("0 的阶乘为 1")
else:
    for i in range(2, num + 1):
        factorial = factorial * i
    print(" %d 的阶乘为 %d" %(num, factorial))