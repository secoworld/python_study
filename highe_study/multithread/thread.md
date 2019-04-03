# 多线程的优点
1. 可以将运行时间长的程序放在后台进行
2. 加快运行速度
3. 等待用户输入时，可以运行处理其他的数据



# Python 线程

Python中使用线程的方式 ：使用类或函数包装线程   

1. 调用`_thread` 模块
2. 创建新的线程
```
_thread.start_new_thread ( function, args[, kwargs] )
```
* function  : 调用的函数
* args      ： 传递的参数