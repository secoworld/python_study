#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @file     : test_swap.py
# @suthor   : longtao
# @date     : 2019-03-28
# @version  : 1.0
# @desc     : 将输入的数字交换

#输入x, y
x = int(input("请输入x : "))
y = int(input("请输入y ："))

#交换x，y
x = x + y
y = x - y
x = x - y

#输出交换后的结果
print("x交换后为：%d" %x)
print("y交换后为：%d" %y)
