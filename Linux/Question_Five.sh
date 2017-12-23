设计一个shell程序，添加一个新组为class1，然后添加属于这个组的30个用户，用户名的形式为stdxx，其中xx从01到30。

#!/bin/bash

groupadd class1

for (( i= 1;i<= 30;i= i+1 ))
    do
        if [ $i -le 9 ]
            then
                name=std0$i               
            else
                name=std$i
        fi
        useradd -g class1 $name
        echo "123" | passwd --stdin "$name"
        echo $i 
    done
