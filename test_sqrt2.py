#!/usr/bin/python3
# -*- coding : UTF-8 -*-
# @file     : test_sqrt2.py
# @author   : longtao
# @date     : 2019-03-28
# @version  : 1.0
# @decr     : 计算二次方程 a*x**2 + b*x + c = 0

#导入cmath 复杂数学运算库
import cmath

#输入a, b, c 三个数
a = float(input("输入a: "))
b = float(input("输入b："))
c = float(input("输入c: "))

#计算
d = (b**2) - (4*a*c)

#两种求解方式
sol1 = (-b + cmath.sqrt(d))/(2*a)
sol2 = (-b - cmath.sqrt(d))/(2*a)

#输出结果
print("结果1：{0}, 结果2：{1}".format(sol1, sol2))