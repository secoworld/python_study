#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @file     : test_temp.py
# @author   : longtao
# @date     : 2019-03-28
# @version  : 1.0
# @desc     : 将温度转变成华氏温度

#输入温度
temp = float(input("请输入温度： "))

#温度转换
fahrenheit = (temp * 1.8) + 32
print("%.1f 摄氏温度转换为华氏温度为： %.1f" %(temp, fahrenheit))
