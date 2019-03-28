#!/usr/bin/python3
# -*- coding : UTF-8 -*-
# @file     : test_triangle.py
# @author   : longtao
# @date     : 2019-03-28
# @version  : 1.0
# @desc     : 计算三角形面积

#输入三边长度
a = float(input("请输入第一边长度： "))
b = float(input("请输入第二边长度： "))
c = float(input("请输入第三边长度： "))

#计算半周长
s = (a + b + c)/2

#计算三角形面积
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

#输出面积
print("三角形的面积为: {0}".format(area))