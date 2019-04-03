#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @file     : smtp.py
# @author   : longtao
# @date     : 2019-04-03
# @des      : python3使用SMTP发送邮件

#导入模块
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#使用第三方邮件发送
mail_host = "smtp.163.com"
mail_user = "chinaliulongtao@163.com"
mail_pass = "longtao1996"
mail_to = "952632352@qq.com"

content = "这是一封测试邮件"
subject = "测试使用"

#发送HTML邮件
content = '<p>这是一个测试邮件</p> \
    <p><a href="http://www.runoob.com">这是一个链接</a></p> \
    '

#创建一个带附件的实例
message = MIMEMultipart()
#message = MIMEText(content, 'html', 'utf-8')
message['From'] = mail_user
message['To'] = mail_to
message['Subject'] = subject

#邮件的正文内容
message.attach(MIMEText(content, 'html', 'utf-8'))

#构建附件，传输本目录中的test.txt
att1 = MIMEText(open(r'E:\MyFile\Program\Python\python_study\highe_study\SMTP\1.txt', 'rb').read(), 'base64', 'utf-8')
#att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
#filename 即是邮件显示的名字
att1["Content-Disposition"] = 'attachment; filename = "test.txt"'
message.attach(att1)

try:
    smt = smtplib.SMTP()
    smt.connect(mail_host, 25)
    smt.login(mail_user, mail_pass)
    smt.sendmail(mail_user, mail_to, message.as_string())
    print("邮件发送成功")
except:
    print("邮件发送失败")