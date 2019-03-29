#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @file     : test_if.py
# @author   : longtao   
# @date     : 2019-03-29
# @version  : 1.0
# @desc     : if语句的学习


#用户输入数字
num = float(input("请输入一个数字："))

if num >= 0:
    if num == 0:
        print("零")
    else:
        print("正数")
else:
    print("负数")