#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @file     : server.py
# @author   : longtao
# @date     : 2019-04-03
# @des      : socket服务端

#导入sys、socket模块
import sys, socket

#创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#获取本地主机名
host = socket.gethostname()

#设置端口
port = 9999

#绑定端口
s.bind((host, port))

while True:
    #建立客户端连接
    clientsockt, addr = serversocket.accpet()

    print("连接地址为： %s", %str(addr))

    msg= "欢迎光临本站 ！" + "\r\n"
    clientsockt.send(msg.encode('utf-8'))
    clientsockt.close()