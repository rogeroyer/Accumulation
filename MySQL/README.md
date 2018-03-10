## 数据库

- [更改wamp MySQL密码](http://blog.csdn.net/wuyan_meixin/article/details/26217087)

- mysql新建用户
> CREATE USER 'username'@'host' IDENTIFIED BY 'password';
- 授权访问数据库
> GRANT ALL PRIVILEGES ON *.*TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;

- mysql为用户授权
```mysql
mysql>create database phplampDB;
//授权phplamp用户拥有phplamp数据库的所有权限。
mysql>grant all privileges on phplampDB.* to phplamp@localhost identified by '1234';
//刷新系统权限表
mysql>flush privileges;
//如果想指定部分权限给一用户，可以这样来写:
mysql>grant select,update on phplampDB.* to phplamp@localhost identified by '1234';
//刷新系统权限表。
mysql>flush privileges;
```

***

#### [python连接数据库](http://www.cnblogs.com/wt11/p/6141225.html)
```python
import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='roger', passwd='roger', db='roger_db', charset='gb2312')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from selectclassinfo")

# 获取剩余结果的第一行数据
row_1 = cursor.fetchone()
print(row_1)
# 获取剩余结果前n行数据
# row_2 = cursor.fetchmany(3)

# 获取剩余结果所有数据
# row_3 = cursor.fetchall()

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update tb7 set pass = '123' where nid = %s", (11,))

# 执行SQL，并返回受影响行数,执行多次
# effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])


# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
```
