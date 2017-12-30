#!/bin/bash
# 先对系统进行判断，如果是Cent OS 64位，就继续运行
platform=`uname -i`
if [ $platform != "x86_64" ];then 
	echo "this script is only for 64bit Operating System !"
	exit 1
fi
echo "the platform is ok"

# 先将系统的安装源设置为网易的
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
wget http://mirrors.163.com/.help/CentOS6-Base-163.repo -O /etc/yum.repos.d/CentOS-Base.repo

# 禁用GSSAPI来认证，也禁用DNS反向解析，加快SSH登陆速度
sed -i 's/^GSSAPIAuthentication yes$/GSSAPIAuthentication no/' /etc/ssh/sshd_config
sed -i 's/#UseDNS yes/UseDNS no/' /etc/ssh/sshd_config
service sshd restar

# 将系统同时打开的文件个数增大
echo "ulimit -SHn 102400" >> /etc/rc.local
cat >> /etc/security/limits.conf << EOF
*           soft   nofile       65535
*           hard   nofile       65535
EOF

# 优化一些内核参数
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
net.ipv4.tcp_max_orphans = 3276800
net.ipv4.tcp_max_syn_backlog = 262144
net.core.wmem_default = 8388608
net.core.rmem_default = 8388608
EOF
/sbin/sysctl -p

# 关闭selinux
sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config


# 调整删除字符的按键为backspace（某些系统默认是delete）
echo 'stty erase ^H' >> /etc/profile

# 打开vim的语法高亮
echo "syntax on" >> /root/.vimrc

# 关闭没用的服务
chkconfig bluetooth off
chkconfig cups off

# 关闭IPv6
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
