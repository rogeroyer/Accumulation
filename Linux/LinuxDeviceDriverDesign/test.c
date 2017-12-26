#include <sys/types.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#define MAX_SIZE 1024

int main(void)
{
	int fd;
	char buf[MAX_SIZE];
	char get[MAX_SIZE];
	char devName[20], dir[50] = "/dev/";
	system("ls /dev/");
	printf("Please input the device's name you wanna to use :");
	gets(devName);
	strcat(dir, devName);
	fd = open(dir, O_RDWR | O_NONBLOCK);
	if (fd != -1)
	{
		read(fd, buf, sizeof(buf));
		printf("The device was inited with a string : %s\n", buf);
		 /* 测试写 */
		printf("Please input a string  :\n");
		gets(get);
		write(fd, get, sizeof(get));
		/* 测试读 */
		read(fd, buf, sizeof(buf)); 
		system("dmesg");
		printf("\nThe string in the device now is : %s\n", buf);
		close(fd);
		return 0;
	}
	else
	{
		printf("Device open failed\n");
		return -1;
	}
}
