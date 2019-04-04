from django.shortcuts import render
from django.shortcuts import HttpResponse 
from login import models    #导入models文件

# Create your views here.

user_list = []
temp = {}

#定义index函数
def index(request):
    #return HttpResponse('Hello word!')  #不能直接返回字符串，需要进行封装
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #将数据存入数据库中
       models.UserInfo.objects.create(user=username, pwd=password)      ## python提示找不到objects 
       models.UserInfo.

    #从数据库中读取所有的数据，注意缩进
    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html', {'date': user_list})    #返回网页

