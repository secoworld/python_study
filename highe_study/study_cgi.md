# CGI-Python 学习

## 安装Apache服务器

我使用的系统是Ubuntu，故而其他系统可能有些不同，可自行Google查询。  

更新Ubuntu软件列表
```
sudo apt update
```
安装apache2  
```
sudo apt-get install apache2
```
安装完成后，可以使用systemctl查看是否安装成功,查看服务器运行状态。
```
systemctl status apache2
```
---
## 配置CGI
1.在web目录下新建cgi文件夹
```
sudo mkdir /var/www/cgi-bin/
```
2.将/etc/apache/ 下的一些文件. 其中较为关注的主要有available和enabled，其中我们配置的CGI并没有被包含在enabled内，而且enabled中的


主要的配置都是在/etc/apache2/conf-enabled中,可以看到CGI的配置文件server-cgi-bin.conf就是位于这个文件夹中。
将
```
ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
<Directory "/usr/lib/cgi-bin">
```
改为：
```
ScriptAlias /cgi-bin/ /var/www/cgi-bin/
<Directory "/var/www/cgi-bin">
```
3.然后，再把/etc/apache2/mods-available/cgi.load(cgid.load)  建软件链接到/etc/apache2/mods-enalbed/cgi.load(cgid.load).  建软链接用  “ln  -s  源文件 目标文件”
```
ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enalbed/cgi.load
```


4.打开/etc/apache2/sites-enabled/000-default.conf 将w文件指向改为
```
ServerAdmin webmaster@localhost
DocumentRoot /var/www/
```
