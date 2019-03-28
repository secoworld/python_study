#!/usr/bin/python3
# -*-  coding : TTF-8 -*-
# @file     : test1.py
# @author   : longtao
# @date     : 2019-03-28
# @version  : 1.0
# @desc     : 数字求和


#用户输入数字
num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")

#求和
sum = float(num1) + float(num2)

#显示结果
print("数字{0}, 数字{1}, 相加结果为{2}".format(num1, num2, sum))