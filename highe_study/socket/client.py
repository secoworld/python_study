#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @file     : client.py
# @author   : longtao
# @date     : 2019-04-03
# @des      : socket客户端

#导入sys、socket模块
import sys, socket

#创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#获取本地主机名
host = socket.gethostname()

#设置端口
port = 9999

#连接服务器
s.connect((host, port))

#接受小于1024个字节数据
msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))