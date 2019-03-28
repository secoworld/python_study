#!/usr/bin/python3
# -*- coding : UTF-8 -*-
# @file     : test_sqrt.py
# @author   : longtao
# @date     : 2019-03-28
# @version  : 1.0
# @desc     : 求平方根

#输入数字
num = float(input("请输入一个数字："))

#开方
num_sqrt = num ** 0.5

#输出
print("输入的数字为：{0}, 平方根为：{1}".format(num, num_sqrt))
