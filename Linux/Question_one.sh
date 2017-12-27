#!/bin/bash
#author
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
