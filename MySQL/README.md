## 数据库

- [更改wamp MySQL密码](http://blog.csdn.net/wuyan_meixin/article/details/26217087)

- mysql新建用户
> CREATE USER 'username'@'host' IDENTIFIED BY 'password';

- mysql为用户授权
```mysql
mysql>create database phplampDB;
//授权phplamp用户拥有phplamp数据库的所有权限。
mysql>grant all privileges on phplampDB.* to phplamp@localhost identified by '1234';
//刷新系统权限表
mysql>flush privileges;
```

***
