from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    #添加路由地址，将url指向index()函数
]