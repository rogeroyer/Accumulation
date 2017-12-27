## 对脚本的内容做一下说明： 

- 先对系统进行判断，如果是Cent OS 64位，就继续运行。
- 先将系统的安装源设置为网易的（网易的安装源算是国内比较稳定的）
- 安装epel的源和rpmforge的源，利用第三方的源来让yum安装起来更方便
- 更新软件
- 设置为每天凌晨四点进行时间同步（跟国家授时中心的服务器进行时间同步）
- 将系统同时打开的文件个数增大
- 将ctrl alt delete键进行屏蔽，防止误操作的时候服务器重启
- 关闭selinux
- 禁用GSSAPI来认证，也禁用DNS反向解析，加快SSH登陆速度
- 优化一些内核参数
- 调整删除字符的按键为backspace（某些系统默认是delete）
- 打开vim的语法高亮
- 取消生成whatis数据库和locate数据库
- 关闭没用的服务
- 关闭IPv6

```shell
#!/bin/bash
#author suzezhi
#this script is only for CentOS 6
#check the OS

platform=`uname -i`
if [ $platform != "x86_64" ];then 
echo "this script is only for 64bit Operating System !"
exit 1
fi
echo "the platform is ok"
version=`lsb_release -r |awk '{print substr($2,1,1)}'`
if [ $version != 6 ];then
echo "this script is only for CentOS 6 !"
exit 1
fi
cat << EOF
+---------------------------------------+
|   your system is CentOS 6 x86_64      |
|      start optimizing.......          |
+---------------------------------------
EOF

#make the 163.com as the default yum repo
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
wget http://mirrors.163.com/.help/CentOS6-Base-163.repo -O /etc/yum.repos.d/CentOS-Base.repo

#add the third-party repo
#add the epel
rpm -Uvh http://download.Fedora.RedHat.com/pub/epel/6/x86_64/epel-release-6-5.noarch.rpm 
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6

#add the rpmforge
rpm -Uvh http://packages.sw.be/rpmforge-release/rpmforge-release-0.5.2-2.el6.rf.x86_64.rpm
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-dag

#update the system and set the ntp
yum clean all
yum -y update glibc\*
yum -y update yum\* rpm\* python\* 
yum -y update
yum -y install ntp
echo "* 4 * * * /usr/sbin/ntpdate 210.72.145.44 > /dev/null 2>&1" >> /var/spool/cron/root
service crond restart

#set the file limit
echo "ulimit -SHn 102400" >> /etc/rc.local
cat >> /etc/security/limits.conf << EOF
*           soft   nofile       65535
*           hard   nofile       65535
EOF

#set the control-alt-delete to guard against the miSUSE
sed -i 's#exec /sbin/shutdown -r now#\#exec /sbin/shutdown -r now#' /etc/init/control-alt-delete.conf

#disable selinux
sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config

#set ssh
sed -i 's/^GSSAPIAuthentication yes$/GSSAPIAuthentication no/' /etc/ssh/sshd_config
sed -i 's/#UseDNS yes/UseDNS no/' /etc/ssh/sshd_config
service sshd restart

#tune kernel parametres
cat >> /etc/sysctl.conf << EOF
net.ipv4.tcp_fin_timeout = 1
net.ipv4.tcp_keepalive_time = 1200
net.ipv4.tcp_mem = 94500000 915000000 927000000
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_timestamps = 0
net.ipv4.tcp_synack_retries = 1
net.ipv4.tcp_syn_retries = 1
net.ipv4.tcp_tw_recycle = 1
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.core.netdev_max_backlog = 262144
net.core.somaxconn = 262144
net.ipv4.tcp_max_orphans = 3276800
net.ipv4.tcp_max_syn_backlog = 262144
net.core.wmem_default = 8388608
net.core.rmem_default = 8388608
EOF
/sbin/sysctl -p

#define the backspace button can erase the last character typed
echo 'stty erase ^H' >> /etc/profile
echo "syntax on" >> /root/.vimrc

#stop some crontab
mkdir /etc/cron.daily.bak
mv /etc/cron.daily/makewhatis.cron /etc/cron.daily.bak
mv /etc/cron.daily/mlocate.cron /etc/cron.daily.bak
chkconfig bluetooth off
chkconfig cups off
chkconfig ip6tables off

#disable the ipv6
cat > /etc/modprobe.d/ipv6.conf << EOFI
alias net-pf-10 off
options ipv6 disable=1
EOFI
echo "NETWORKING_IPV6=off" >> /etc/sysconfig/network
cat << EOF
+-------------------------------------------------+
|               optimizer is done                 |
|   it's recommond to restart this server !       |
+-------------------------------------------------+
EOF
```

`[参考网站]`(http://www.linuxde.net/2011/12/5756.html)
