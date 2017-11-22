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
