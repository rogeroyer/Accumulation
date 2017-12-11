
// dynamic programing.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <time.h>
#include <stdio.h>
#define N 11

const int max_weight = 200; //最大权值
int weight[N] = {0, 19,23,12,34,24,34,56,24,53,35}; //背包重量
int value[N] = {0, 57,68,87,17,12,21,31,42,14,15}; //背包价值
int flag[N] = {0};
int count = 0;

//函数功能:求最大值
//参数:将要做比较的两个数
int max(int a,int b)
{
	return a > b ? a : b;
}

//函数功能:求最大值
//参数:背包重量 | 背包价值
int solve(int i, int j)
{
	int value_one = 0;
	int value_two = 0;
	if((j >= 0 && i == 0) || (i >= 0 && j == 0))
		return 0;

	if (j < weight[i])
		return solve(i - 1, j);
	else {
		count++;
		printf("\ncount=%d\n",count);

		//printf("%d is selected!\n", i);
		//return max(solve(i - 1, j), (value[i] + solve(i-1, j-weight[i])));
		value_one = solve(i - 1, j);
		value_two = value[i] + solve(i-1, j-weight[i]);
		if(value_one > value_two) {
			return value_one;
		}
		else
		{
		//	printf("%d is selected!\n", i);
			flag[i] = 1;
			return value_two;
		}
	}
}

int main()
{ 
	clock_t start,end;
	start = clock(); 
	
	int max_value = solve(N, max_weight);
	printf("%d\n", max_value);
	
	for(int i = 0;i < N;i++)
	{
		printf("%4d",flag[i]);
	}

	printf("\ncount=%d\n",count);

	end = clock();  
	printf("\ntime=%f\n",(double)(end-start)/CLK_TCK); 

	return 0;
}
