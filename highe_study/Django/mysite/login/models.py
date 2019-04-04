from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user = models.CharField(max_length=32)  #设置用户名字符长度为32
    pwd = models.CharField(max_length=32)   #设置密码长度为32

