#include <stdlib.h>
#include <stdio.h> 
#include <time.h>
#include<windows.h>
#define N 40 
typedef struct games
{
	char name[10];
	int flag;
}G;

int main()
{
	char ch;
	int i = 0, num = 0,count = 0;
	G number[N] = {
		{"电饭锅", 0},
		{"纯净水", 0},
		{"面条", 0}, 
		{"电视机", 0},
		{"沙发", 0}, 
		{"拖把", 0},
		{"衣柜", 0},
		{"书桌", 0},
		{"化妆品", 0},
		{"吉他", 0},
		{"面具", 0},
		{"江小白", 0},
		{"玻璃杯", 0},
		{"地图", 0},
		{"蜡烛", 0},
		{"电子表", 0},
		{"地球仪", 0},
		{"CPU", 0},
		{"灭火器", 0},
		{"象棋", 0},
		{"篮球", 0},
		{"网球", 0},
		{"火车", 0},
		{"战斗机", 0},
		{"猫", 0},
		{"狗", 0},
		{"猪", 0},
		{"熊猫", 0},
		{"自由女神", 0},
		{"长城", 0}, 
		{"钢笔", 0},
		{"老年机", 0},
		{"APP", 0},
		{"编译器", 0},
		{"数据", 0},
		{"数组", 0},
		{"函数", 0},
		{"循环", 0},
		{"字符串", 0},
		{"C语言", 0}
	};
	
//	for (i = 0;i < 10;i++) {
//		printf("%s : %d\n",number[i].name, number[i].flag);
//	}
	
	while(count < N/2) {
		srand(time(NULL));
		system("cls");
		num = rand()%N;
		while(number[num].flag != 0 && num < N-1)
		{
			num += 1;
		}
		if(number[num].flag == 0)
		{
			printf("\n\n\n\n\n\n\t\t\t                First Group\n");
			printf("\n\t\t\t****************************************\n\n");
	//		printf("\t\t\t*                  %d\t\t       *\n", num);
			printf("\t\t\t                  %s\t\t       \n\n", number[num].name);
			printf("\t\t\t****************************************\n");
			count++;
			number[num].flag = 1;
			Sleep(35000);
//			ch = getch();
			printf("\a"); 
			Sleep(1000);
			printf("\a"); 
			Sleep(1000);
			printf("\a"); 
			Sleep(1000);
			printf("\a"); 
			Sleep(1000);
			printf("\a");
			Sleep(1000);
			printf("\a");
		}
	}
	printf("\n\t\t\t              Game over!\n\n\n\n");
	
	
	ch = getch();
	system("cls");
	while(count < N) {
		srand(time(NULL));
		system("cls");
		num = rand()%N;
		
		while(number[num].flag != 0 && num < N-1)
		{
			num += 1;
		}
		if(number[num].flag == 0)
		{
			printf("\n\n\n\n\n\n\t\t\t                Second Group\n");
			printf("\n\t\t\t****************************************\n\n");
	//		printf("\t\t\t*                  %d\t\t       *\n", num);
			printf("\t\t\t                  %s\t\t       \n\n", number[num].name);
			printf("\t\t\t****************************************\n");
			count++;
			number[num].flag = 1;
			Sleep(35000);
//			ch = getch();
			printf("\a"); 
			Sleep(1000);
			printf("\a"); 
			Sleep(1000);
			printf("\a"); 
			Sleep(1000);
			printf("\a"); 
			Sleep(1000);
			printf("\a");
			Sleep(1000);
			printf("\a");
		}
	}
	printf("\n\t\t\t              Game over!\n\n\n\n");
	ch = getch();
    return 0;
}
