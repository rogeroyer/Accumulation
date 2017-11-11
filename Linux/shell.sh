我们在运维中，尤其是linux运维，都知道脚本的重要性，脚本会让我们的 运维事半功倍，所以学会写脚本是我们每个linux运维必须学会的一门功课，这里收藏linux运维常用的脚本。如何学好脚本，最关键的是就是大量的练习 和实践。根据以下脚本我们可以拓展，这样我们提高的很快！举一反三！
  
1．用Shell编程，判断一文件是不是字符设备文件，如果是将其拷贝到 /dev 目录下。
 
参考程序：
C代码  收藏代码
#!/bin/sh 
FILENAME= 
echo “Input file name：” 
read FILENAME 
if [ -c "$FILENAME" ] 
then 
cp $FILENAME /dev 
fi  
  
2．设计一个shell程序，添加一个新组为class1，然后添加属于这个组的30个用户，用户名的形式为stdxx，其中xx从01到30。
 
参考答案：
C代码  收藏代码
#!/bin/sh 
i=1 
groupadd class1 
while [ $i -le 30 ] 
do 
if [ $i -le 9 ] ;then 
USERNAME=stu0${i} 
else 
USERNAME=stu${i} 
fi 
useradd $USERNAME 
mkdir /home/$USERNAME 
chown -R $USERNAME /home/$USERNAME 
chgrp -R class1 /home/$USERNAME 
i=$(($i+1)) 
done 
 
3．编写shell程序，实现自动删除50个账号的功能。账号名为stud1至stud50。
  
参考程序：
C代码  收藏代码
#!/bin/sh 
i=1 
while [ $i -le 50 ] 
do 
userdel -r stud${i} 
i=$(($i+1 )) 
done 
 
4．某系统管理员需每天做一定的重复工作，请按照下列要求，编制一个解决方案：
（1）在下午4 :50删除/abc目录下的全部子目录和全部文件；
（2）从早8:00～下午6:00每小时读取/xyz目录下x1文件中每行第一个域的全部数据加入到/backup目录下的bak01.txt文件内；
（3）每逢星期一下午5:50将/data目录下的所有目录和文件归档并压缩为文件：backup.tar.gz；
（4）在下午5:55将IDE接口的CD-ROM卸载（假设：CD-ROM的设备名为hdc）；
（5）在早晨8:00前开机后启动。
 
参考答案:
解决方案：
（1）用vi创建编辑一个名为prgx的crontab文件；
（2）prgx文件的内容：
C代码  收藏代码
50 16 * * * rm -r /abc/* 
0 8-18/1 * * * cut -f1 /xyz/x1 >;>; /backup/bak01.txt 
50 17 * * * tar zcvf backup.tar.gz /data 
55 17 * * * umount /dev/hdc 
  
（3）由超级用户登录，用crontab执行 prgx文件中的内容：
root@xxx:#crontab prgx；在每日早晨8:00之前开机后即可自动启动crontab。
 
5．设计一个shell程序，在每月第一天备份并压缩/etc目录的所有内容，存放在/root/bak目录里，且文件名为如下形式yymmdd_etc，yy为年，mm为月，dd为日。Shell程序fileback存放在/usr/bin目录下。
  
参考答案：
（1）编写shell程序fileback：
C代码  收藏代码
#!/bin/sh 
DIRNAME=`ls /root | grep bak` 
if [ -z "$DIRNAME" ] ; then 
mkdir /root/bak 
cd /root/bak 
fi 
YY=`date +%y` 
MM=`date +%m` 
DD=`date +%d` 
BACKETC=$YY$MM$DD_etc.tar.gz 
tar zcvf $BACKETC /etc 
echo “fileback finished!” 
  
（2）编写任务定时器：
C代码  收藏代码
echo “0 0 1 * * /bin/sh /usr/bin/fileback” >; /root/etcbakcron 
crontab /root/etcbakcron 
或使用crontab -e 命令添加定时任务： 
0 1 * * * /bin/sh /usr/bin/fileback 
  
6．有一普通用户想在每周日凌晨零点零分定期备份/user/backup到/tmp目录下，该用户应如何做？
  
参考答案：
  
（1）第一种方法：
C代码  收藏代码
用户应使用crontab –e 命令创建crontab文件。格式如下： 
0 0 * * sun cp –r /user/backup /tmp 
  
（2）第二种方法：
用户先在自己目录下新建文件file，文件内容如下：
C代码  收藏代码
0 * * sun cp –r /user/backup /tmp 
然后执行 crontab file 使生效。
  
7.设计一个Shell程序，在/userdata目录下建立50个目录，即user1～user50，并设置每个目录的权限，其中其他用户的权限为：读；文件所有者的权限为：读、写、执行；文件所有者所在组的权限为：读、执行。
  
参考答案: 建立程序 Pro16如下：
C代码  收藏代码
#!/bin/sh 
i=1 
while [ i -le 50 ] 
do 
if [ -d /userdata ];then 
mkdir -p /userdata/user$i 
chmod 754 /userdata/user$i 
echo “user$i” 
let “i = i + 1″ （或i=$（（$i＋1）） 
else 
mkdir /userdata 
mkdir -p /userdata/user$i 
chmod 754 /userdata/user$i 
echo “user$i” 
let “i = i + 1″ （或i=$（（$i＋1）） 
fi 
done 
  
8、mysql备份实例，自动备份mysql，并删除30天前的备份文件
C代码  收藏代码
#!/bin/sh 
   
#auto backup mysql 
#wugk  2012-07-14 
#PATH DEFINE 
   
BAKDIR=/data/backup/mysql/`date +%Y-%m-%d` 
MYSQLDB=www 
MYSQLPW=backup 
MYSQLUSR=backup 
   
if[ $UID -ne 0 ];then 
echo This script must use administrator or root user ,please exit! 
sleep 2 
exit 0 
fi 
   
if[ ! -d $BAKDIR ];then 
mkdir -p $BAKDIR 
else 
echo This is $BAKDIR exists ,please exit …. 
sleep 2 
exit 
fi 
   
###mysqldump backup mysql 
   
/usr/bin/mysqldump -u$MYSQLUSR -p$MYSQLPW -d $MYSQLDB >/data/backup/mysql/`date +%Y-%m-%d`/www_db.sql 
   
cd $BAKDIR ; tar -czf  www_mysql_db.tar.gz *.sql 
   
cd $BAKDIR ;find  . -name “*.sql” |xargs rm -rf[ $? -eq 0 ]&&echo “This `date +%Y-%m-%d` RESIN BACKUP is SUCCESS” 
   
cd /data/backup/mysql/ ;find . -mtime +30 |xargs rm -rf 
  
9、自动安装Nginx脚本，采用case方式，选择方式，也可以根据实际需求改成自己想要的脚本
C代码  收藏代码
#!/bin/sh 
   
###nginx install shell 
###wugk 2012-07-14 
###PATH DEFINE 
   
SOFT_PATH=/data/soft/ 
NGINX_FILE=nginx-1.2.0.tar.gz 
DOWN_PATH=http://nginx.org/download/ 
   
if[ $UID -ne 0 ];then 
echo This script must use administrator or root user ,please exit! 
sleep 2 
exit 0 
fi 
   
if[ ! -d $SOFT_PATH ];then 
mkdir -p $SOFT_PATH 
fi 
   
download () 
{ 
cd $SOFT_PATH ;wget $DOWN_PATH/$NGINX_FILE 
} 
   
install () 
{ 
yum install pcre-devel -y 
cd $SOFT_PATH ;tar xzf $NGINX_FILE ;cd nginx-1.2.0/ &&./configure –prefix=/usr/local/nginx/ –with-http_stub_status_module –with-http_ssl_module 
[ $? -eq 0 ]&&make &&make install 
} 
   
start () 
{ 
lsof -i :80[ $? -ne 0 ]&&/usr/local/nginx/sbin/nginx 
} 
   
stop () 
{ 
ps -ef |grep nginx |grep -v grep |awk ‘{print $2}’|xargs kill -9 
} 
   
exit () 
{ 
echo $? ;exit 
} 
   
###case menu ##### 
   
case $1 in 
download ) 
download 
;; 
   
install ) 
install 
;; 
   
start ) 
start 
;; 
stop ) 
stop 
;; 
   
* ) 
   
echo “USAGE:$0 {download or install or start or stop}” 
exit 
esac 
  
10、批量解压tar脚本，批量解压zip并且建立当前目录。
C代码  收藏代码
#!/bin/sh 
PATH1=/tmp/images 
PATH2=/usr/www/images 
for i in `ls ${PATH1}/*` 
do 
tar xvf  $i  -C $PATH2 
done 
  
这个脚本是针对所有tar文件在一个目录，但是实际情况中，有可能在下级或者更深的目录，我们可以使用find查找
C代码  收藏代码
#!/bin/sh 
PATH1=/tmp/images 
PATH2=/usr/www/images 
for i in `find  $PATH1  -name  ”*.tar” ` 
do 
tar xvf  $i  -C $PATH2 
done 
  
如何是zip文件，例如123189.zip 132342.zip 等等批量文件，默认unzip直接解压不带自身目录，意思是解压123189.zip完当前目录就是图片，不能创建123189目录下并解压，可以用shell脚本实现
C代码  收藏代码
#!/bin/sh 
PATH1=/tmp/images 
PATH2=/usr/www/images 
cd $PATH1 
   
for i in `find  . -name  ”*.zip”|awk  -F.  {print $2} ` 
do 
   
mkdir -p   PATH2$i 
   
unzip -o  .$i.zip  -d   PATH2$i 
done  
  
原创文章转载请注明: Linux常用Shell脚本珍藏 | 专注Unix/Linux领域
  
ssh 批量上传文件
 
上传文件大多数用的是ftp，但是用ftp有一点不好，就是本地和远程的目录要对应，这样就要在多个目录下去切换，这样挺麻烦的，如果不注意的话，很有可能传错。所以想了个办法利用scp来批量上传文件或者目录。
  
一，scp上传不要输入密码
如果要用scp来上传文件，第一步就要去掉scp上传时要输入密码。要不然就没办法批量上传了。具体请参考：ssh 不用输入密码
  
二，ssh批量上传脚本
  
1,要上传的文件列表放到一个test文件中
C代码  收藏代码
root@ubuntu:/home/zhangy# cat test   
/home/zhangy/test/aaa   
/home/zhangy/test/nginx.conf   
     
/home/zhangy/test/test.sql   
/home/zhangy/test/pa.txt   
/home/zhangy/test/password   
  
上面就要上传的文件。
  
2,批量上传的脚本
  
vim file_upload.sh
C代码  收藏代码
#!/bin/sh 
   
DATE=`date +%Y_%m_%d_%H` 
   
if [ $1 ] 
then 
  for file in $(sed '/^$/d' $1)     //去掉空行 
  do 
    if [ -f $file ]                 //普通文件 
    then 
      res=`scp $file $2:$file`      //上传文件 
      if [ -z $res ]                //上传成功 
      then 
        echo $file >> ${DATE}_upload.log   //上传成功的日志 
      fi 
    elif [ -d $file ]              //目录 
    then 
      res=`scp -r $file $2:$file` 
      if [ -z $res ] 
      then 
        echo $file >> ${DATE}_upload.log 
      fi 
    fi 
  done 
else 
  echo "no file" >> ${DATE}_error.log 
fi 
  
上传成功后，返回的是一个空行，上传不成功，什么都不返回
  
3，上传的格式
C代码  收藏代码
./file_upload.sh test 192.168.1.13   
test是上传列表文件，192.168.1.13文件要传到的地方。
0
 
转载请注明
作者:海底苍鹰
地址:http://blog.51yip.com/linux/1356.html
  
1. 转换文件大小写：
A script to convert the specified filenames to lower case.
  
C代码  收藏代码
#!/bin/sh 
 # lowerit 
# convert all file names in the current directory to lower case 
# only operates on plain files--does not change the name of directories 
# will ask for verification before overwriting an existing file 
for x in `ls` 
do 
    if [ ! -f $x ]; then 
        continue 
    fi 
    lc=`echo $x  | tr '[A-Z]' '[a-z]'` 
    if [ $lc != $x ]; then 
        mv -i $x $lc 
    fi 
done 
  
  
or
  
C代码  收藏代码
if test $# = 0 
then 
    echo "Usage $0: <files>" 1>&2 
    exit 1 
fi 
   
for filename in "$@" 
do 
    new_filename=`echo "$filename" | tr A-Z a-z` 
    test "$filename" = "$new_filename" && continue 
    if test -r "$new_filename" 
    then 
        echo "$0: $new_filename exists" 1>&2 
    elif test -e "$filename" 
    then 
        mv "$filename" "$new_filename" 
    else 
        echo "$0: $filename not found" 1>&2 
    fi 
done 
  
  
2. 看网站 Watch a Website
  
A script to repeated download a webpage until it matches a regex then notify an e-mail address.
For example to get e-mail when Kesha tickets (not for yourself of course) go on sale you might run:
  
C代码  收藏代码
% watch_website.sh http://ticketek.com.au/ 'Ke[sS$]+ha' andrewt@cse.unsw.edu.au 
   
   
repeat_seconds=300  #check every 5 minutes 
   
if test $# = 3 
then 
    url=$1 
    regexp=$2 
    email_address=$3 
else 
    echo "Usage: $0 <url> <regex>" 1>&2 
    exit 1 
fi 
   
while true 
do 
    if wget -O- -q "$url"|egrep "$regexp" >/dev/null 
    then 
        echo "Generated by $0" | mail -s "$url now matches $regexp" $email_address 
        exit 0 
    fi 
    sleep $repeat_seconds 
done 
  
  
3. 转GIF到PNG convert GIF files to PNG
  
This scripts converts GIF files to PNG files via the intermediate PPM format.
  
C代码  收藏代码
if [ $# -eq 0 ] 
then 
    echo "Usage: $0 files..." 1>&2 
    exit 1 
fi 
   
if ! type giftopnm 2>/dev/null 
then 
    echo "$0: conversion tool giftopnm not found " 1>&2 
    exit 1 
fi 
   
# missing "in ..." defaults to in "$@" 
for f 
do 
    case "$f" in 
    *.gif) 
        # OK, do nothing 
        ;; 
    *) 
        echo "gif2png: skipping $f, not GIF" 
        continue 
        ;; 
    esac 
   
    dir=`dirname "$f"` 
    base=`basename "$f" .gif` 
    result="$dir/$base.png" 
   
    giftopnm "$f" | pnmtopng > $result && echo "wrote $result" 
done 
  
  
4.  计数 Counting
  
A utility script to print the sub-range of integers specified by its arguments.
Useful to use on the command line or from other scripts
  
C代码  收藏代码
if test $# = 1 
then 
    start=1 
    finish=$1 
elif test $# = 2 
then 
    start=$1 
    finish=$2 
else 
    echo "Usage: $0 <start> <finish>" 1>&2 
    exit 1 
fi 
   
for argument in "$@" 
do 
    if echo "$argument"|egrep -v '^-?[0-9]+$' >/dev/null 
    then 
        echo "$0: argument '$argument' is not an integer" 1>&2 
        exit 1 
    fi 
done 
   
number=$start 
while test $number -le $finish 
do 
    echo $number 
    number=`expr $number + 1`    # or number=$(($number + 1)) 
done 
  
  
5. 字频率 Word Frequency
Count the number of time each different word occurs in the files given as arguments.
  
C代码  收藏代码
sed 's/ /\n/g' "$@"|      # convert to one word per line 
tr A-Z a-z|               # map uppercase to lower case 
sed "s/[^a-z']//g"|       # remove all characters except a-z and '   
egrep -v '^$'|             # remove empty lines 
sort|                     # place words in alphabetical order 
uniq -c|                  # use uniq to count how many times each word occurs 
sort -n                   # order words in frequency of occurrance 
 For example
  
  
C代码  收藏代码
% cd /home/cs2041/public_html/lec/shell/examples 
% ./word_frequency.sh dracula.txt|tail 
   2124 it 
   2440 that 
   2486 in 
   2549 he 
   2911 a 
   3600 of 
   4448 to 
   4740 i 
   5833 and 
   7843 the 
  
  
6. Finding
  
Search $PATH for the specified programs
C代码  收藏代码
if test $# = 0 
then 
    echo "Usage $0: <program>" 1>&2 
    exit 1 
fi 
   
for program in "$@" 
do 
    program_found='' 
    for directory in `echo "$PATH" | tr ':' ' '` 
    do 
        f="$directory/$program" 
        if test -x "$f" 
        then 
            ls -ld "$f" 
            program_found=1 
        fi 
    done 
    if test -z $program_found 
    then 
        echo "$program not found" 
    fi 
done 
  
Alternative implementation using while, and a cute use of grep and ||
C代码  收藏代码
if test $# = 0 
then 
    echo "Usage $0: <program>" 1>&2 
    exit 1 
fi 
   
for program in "$@" 
do 
    echo "$PATH"| 
    tr ':' '\n'| 
    while read directory 
    do 
        f="$directory/$program" 
        if test -x "$f" 
        then 
            ls -ld "$f" 
        fi 
    done| 
    egrep '.' || echo "$program not found" 
done 
  
And another implementation using while, and a cute use of grep and ||
C代码  收藏代码
if test $# = 0 
then 
    echo "Usage $0: <program>" 1>&2 
    exit 1 
fi 
for program in "$@" 
do 
    n_path_components=`echo $PATH|tr -d -c :|wc -c` 
    index=1 
    while test $index -le $n_path_components 
    do 
        directory=`echo "$PATH"|cut -d: -f$index` 
        f="$directory/$program" 
        if test -x "$f" 
        then 
            ls -ld "$f" 
            program_found=1 
        fi 
        index=`expr $index + 1` 
    done 
    test -n $program_found || echo "$program not found" 
done 
  
来源： http://www.cse.unsw.edu.au/~cs2041/12s2/lec/shell/examples.notes.html
