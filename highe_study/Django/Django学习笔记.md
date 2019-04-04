# 一、 基本概念
## MVC:是模型(model)－视图(view)－控制器(controller)
	• 模型(model)：定义数据库相关的内容，一般放在models.py文件中。
	
	• 视图(view)：定义HTML等静态网页文件相关，也就是那些HTML、CSS、JS等前端的东西。
	
	• 控制器(controller)：定义业务逻辑相关，就是你的主要代码。


## MTV: 模型-模板-控制器
## WSGI: 
PythonWeb服务器网关接口（Python Web Server Gateway Interface，缩写为WSGI)是Python应用程序或框架和Web服务器之间的一种接口

# 二、 项目实例
## 1. 安装Django
```
pip3 install django
```
使用之前可以升级一下pip3， `python -m pip install --upgrade pip`

安装完成之后可以通过`django-admin help ` 可以看到安装的过程

检查是否存在Django模块
``` shell
pip list
```

## 2. 创建Django项目
1. 可以通过pycharm 或者 vscode创建项目
2. 通过一下命令创建项目
``` shell 
django-admin startproject mysite
```
3. 运行网站，默认端口为`8000`。也可以指定端口`port`和地址`addr`
``` shell
python manage.py runserver [addr:port]
```
## 3. 创建APP
每个Django项目中可以拥有多个APP,可以作为一个大项目的各个模块。所有的APP共享项目的资源   
创建`login`APP
``` python
python manage.py startapp login
```

## 4. 编写路由
路由是在浏览器中输入url，在Django服务器响应中心进行分发url。路由都写在了urls文件中，它将url映射到对应的业务处理上。

简单的urls编写方法如下,在/mysite/urls.py中加入
``` python
from login import views

path('index/', views.index),		#添加到urlpatterns
```
需要在/login/views.py中编写index内容，网页显示内容

或者
在`login`下创建`urls.py`,写入
``` python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
``` 

在`/mysite/urls.py`中导入`include`模块，并且在`urlpatterns`中加入
``` python
path('login/', include('login.urls')),
```

## 5. 编写视图函数
视图函数处理用户的请求，也就是编写业务逻辑，一般业务逻辑和视图都写在了对应的`views.py`中，在`vies.py`中加入
``` python
from django.shortcuts import HttpResponse 

#定义index函数
def index(request):
    return HttpResponse('Hello word!')  #不能直接返回字符串，需要进行封装
```
## 6. 运行服务

## 7. 返回HTML文件
需要将HTML页面返回给用户   
在顶层文件创建`templates`文件夹，新建`index.html`文件，并且在`html`文件中写入一个网页。

修改`/login/views.py`文件，修改`index()`函数。
``` python
#定义index函数
def index(request):
    #return HttpResponse('Hello word!')  #不能直接返回字符串，需要进行封装
    return render(request, 'index.html')    #返回网页
```

在项目的设置中导入tempaltes地址，在`/mysite/setting`中的`TEMPLATES`加入
``` python
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

## 8. 使用静态文件
在Django中将静态文件放在`static`文件夹中    
在顶层文件中创建`static`目录

## 9. 接受用户发送的数据
我们需要接受用户输入的信息。   
修改`index.html`文件，删除原来的内容,重新写入。   
``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
</head>
<body>
    <h1>用户输入:<h1>
    <form action="/index/" method="post" >
        用户名：<input type="text" name="username" /> <br />
        密码：<input type="password" name="password"/><br />
        <input type="submit" value="提交" />
    </form>
</body>
</html>
```

同时更改`login/views.py`中的`index()`内容，
``` python
def index(request):
    #return HttpResponse('Hello word!')  #不能直接返回字符串，需要进行封装
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
    return render(request, 'index.html')    #返回网页
```

当我们输入内容进行提交后，页面将会进入404错误页面。这是由于Django的跨站保护请求，我们需要在`index.html`中加入
``` html
{% csrf_token %}
```

## 10. 返回动态页面
现在将静态页面变成动态页面，将接受到的数据进行处理后，将结果返回给用户。

首先先编写views.py中的内容
``` python
from django.shortcuts import render
from django.shortcuts import HttpResponse 

# Create your views here.

user_list = []

#定义index函数
def index(request):
    #return HttpResponse('Hello word!')  #不能直接返回字符串，需要进行封装
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        temp = ｛'user': username, 'pwd': password｝
        user_list.append(temp)
    return render(request, 'index.html')    #返回网页

```

更改`index.html`文件,在表单后面添加
``` html 
<h1> 用户展示： </h1>
        <table border="1">
            <thead>
                <tr>用户名</tr>
                <tr>密码</tr>
            </thead>
            <tbody>
                {% for item in data %}
                <tr>
                    <td>{{ item.user }}</td>
                    <td>{{ item.pwd }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
```


## 11. 使用数据库   
Django支持多种数据库，通过自身自带的ORM框架操作数据库，并且支持轻量级的sqlite3数据库。

1. 使用数据库之前，首先需要注册APP，在`/mysite/setting.py`中的`INSTALLED_APPS`添加注册的`APP`。在最后加入
``` python
'login',
```
如果不进行注册，数据库不知道给哪个APP创建表单。   
如果我们使用默认的sqlite3，则不需要修改。   

2. 然后进行修改`/login/models.py`,也就是MTV中的M。
``` python
class UserInfo(models.Model):
    user = models.CharField(max_length=32)  #设置用户名字符长度为32
    pwd = models.CharField(max_length=32)   #设置密码长度为32
```

3. 运行命令创建数据库的表。
``` shell
python manage.py makemigrations
python manage.py migrate
```

4. 修改`/login/views.py`
``` python

```

