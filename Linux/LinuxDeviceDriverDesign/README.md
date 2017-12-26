## 第二部分

### Linux设备驱动程序设计

- 编写一个linux的设备驱动程序（为简单起见，建议编写一个字符设备驱动程序），必须满足如下要求：
      - 需要有一个设备驱动程序
      - 需要有一个测试程序，以验证设备驱动程序的功能。


- [参考文档（首选）](http://blog.csdn.net/creazyapple/article/details/7290680)
- [参考文档](https://www.cnblogs.com/chen-farsight/p/6155518.html#unit3.1.5)

***

### 步骤演示

- 编译驱动程序
  - 控制台下进入文件所在目录，管理员权限登陆，输入命令`make`

- 装载模块    
  - 命令`insmod devDrv.ko`    
  - 命令`lsmod`查看系统模块是否多了一个`devDrv`

- 查看系统日志信息`dmesg`

- 测试驱动程序
  - 命令`gcc test.c -o exe`  
  - 生成exe可执行文件，再执行命令`./exe`
