#!/bin/bash
read -p "Please input filename:" filename
# -b判断是否是块设备 -o逻辑或 -c/-u判断是否是字符文件 #
if [ -b $filename -o -c $filename ]; # 注意if后面的空格 # 
then
        echo "$filename is a device file or a charactor file!"
        # cp -a 全复制 #        
        cp -a $filename /dev/
        echo "copy finished!"
else
        echo "$filename is not a device file or a charactor file!!" 
        exit 1
fi


# 命令：man mknod #
# eg:mknod kuaifile b 8 10 #
