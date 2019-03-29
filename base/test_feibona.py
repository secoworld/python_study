#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @file     : test_feibona.py
# @author   : longtao
# @date     : 2019-03-29
# @version  : 1.0
# @desc     : 斐波那数列

#输入需要多少项斐波那数列
num = int(input("请输入需要多少项："))

#初始值
n1 = 0
n2 = 1
count = 1

#计算
if num <= 0:
    print("请输入大于0正整数！")
elif num ==  1:
    print("斐波那契数列为：")
    print(n1)
else:
    print("斐波那契数列为：")
    print(n1, ",", n2, end=",")
    for i in range(3, num+1):
        count = n1 + n2
        n1 = n2
        n2 = count
        print(count, end=",")
