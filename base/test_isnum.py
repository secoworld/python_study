#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @file     : test_isnum.py
# @author   : longtao
# @date     : 2019-03-29
# @version  : 1.0
# @desc     : 判断输入的字符是否是数字


def is_numbers(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except(TypeError, ValueError):
        pass

#测试字符串和数字
print(is_numbers('foo'))    #False
print(is_numbers('1'))      #True
print(is_numbers('1.3'))    #True
print(is_numbers('-1.37'))  #True
print(is_numbers('1e3'))    #True

#测试unicode
#阿拉伯 5
print(is_numbers('。'))     #True
print(is_numbers('四'))     #True

#版权号
print(is_numbers('c'))      #False
