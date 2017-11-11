16.设计一个shell程序，在每月第一天备份并压缩/etc目录的所有内容，存放在/root/bak目录里，且文件名
为如下形式yymmdd_etc，yy为年，mm为月，dd为日。Shell程序fileback存放在/usr/bin目录下。

Method_one:
vim /usr/bin/fileback.sh
#!/bin/bash
#fileback.sh
#file executable: chmod 755 fileback.sh
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
filename=`date +%y%m%d`_etc.tar.gz
cd /etc/
tar -zcvf $filename *
mv $filename /root/bak/
------------------------------------------------------
vim /etc/crontab 加入
* * 1 * * root ./fileback.sh &

http://blog.csdn.net/lile269/article/details/6658885



Method_two:
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
echo "fileback finished!"
