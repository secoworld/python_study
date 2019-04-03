# SMTP 简单邮件传输协议

## 发送流程
1. 导入相应的模块   
```
import smtplib
from email.mime.text import MIMEText
from email.header import Header
```
2. 设置发送内容、发送地址、接受者、主题等
3. 设置邮箱的SMTP代理，使用代理授权密码进行发送
4. 建立SMTP对象，连接远程邮箱smtp地址和端口
5. 登录邮箱，发送邮件

## 发送HTML网页
需要将message 中的格式改为`html`格式.
```
message = MIMEText(content, 'html', 'utf-8')
```
content的内容为html。

## 带附件的邮件
1. 首先导入`MIMEMultipart`模块
```
from email.mime.multipart import MIMEMultipart
```

2. 在开始时，构建一个带附件的实例
```
message = MIMEMultipart()
```
3. 其他发件人、收件人如上即可。

4. 将正文内容替换为
```
#邮件的正文内容
message.attach(MIMEText(content, 'html', 'utf-8'))
```

5. 构建附件
```
#构建附件，传输本目录中的test.txt
att1 = MIMEText(open("test.txt", 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
#filename 即是邮件显示的名字
att1["Content-Disposition"] = 'attachment; filename = "test.txt"'
message.attach(att1)
```

6. 登录、发送过程并没有更改