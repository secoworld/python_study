#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @file     : test_isleap.py
# @author   : longtao
# @date     : 2019-03-29
# @version  : 1.0
# @desc     : 判断年份是否是闰年    能被4整除但是不能被100整除的年份， 或者能够被400整除的年份


#用户输入一个年份
year = int(input("请输入一个年份："))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("%d 为闰年" %year)
else:
    print("%d 不是闰年" %year)