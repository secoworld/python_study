#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @file     : test_prime.py
# @author   : longtao
# @date     : 2019-03-29
# @version  : 1.0
# desc      : 输出指定区间的质数

#输入区间的范围
lower = int(input("输入区间的最小值："))
upper = int(input("输入区间的最大值："))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            print(num)