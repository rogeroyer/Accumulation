#include<stdio.h>

int i = 1;

void move(int n, char from, char to)
{
	printf("The %d th step:move %dth plate from %c to %c\n", i++, n, from, to);
}

void Hanoi(int n, char from, char depend_on, char to)
{
	if(n == 1)
		move(1, from, to);
	else
	{
		Hanoi(n-1, from, to, depend_on);
		move(n, from, to);
		Hanoi(n-1, depend_on, from, to);
	}
}

/*
void move(int n,char from,char to) //将编号为n的盘子由from移动到to
{
	printf("第%d步:将%d号盘子%c---->%c\n",i++,n,from,to);
}
void Hanoi(int n,char from,char denpend_on,char to)//将n个盘子由初始塔移动到目标塔(利用借用塔)
{
    if (n==1)
    move(1,from,to);//只有一个盘子是直接将初塔上的盘子移动到目的地
	else
	{
      Hanoi(n-1,from,to,denpend_on);//先将初始塔的前n-1个盘子借助目的塔移动到借用塔上
	  move(n,from,to);              //将剩下的一个盘子移动到目的塔上
	  Hanoi(n-1,denpend_on,from,to);//最后将借用塔上的n-1个盘子移动到目的塔上
	}
}
*/
void main()
{
	int n;
	printf("Please input the number of plate:\n");
	scanf("%d", &n);
	char x = 'A', y = 'B', z = 'C';
	printf("The situation of moving plate is:\n");
	Hanoi(n, x, y, z);
}
