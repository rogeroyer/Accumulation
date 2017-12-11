// C语言实现0-1背包问题
// 回溯法求解
#include <stdio.h>
 
#define N 3         //物品的数量
#define C 16        //背包的容量
 
int w[N]={10,8,5};  //每个物品的重量
int v[N]={5,4,1};   //每个物品的价值
int x[N]={0,0,0};   //x[i]=1代表物品i放入背包，0代表不放入
 
int CurWeight = 0;  //当前放入背包的物品总重量
int CurValue = 0;   //当前放入背包的物品总价值
 
int BestValue = 0;  //最优值；当前的最大价值，初始化为0
int BestX[N];       //最优解；BestX[i]=1代表物品i放入背包，0代表不放入
 
//t = 0 to N-1
void backtrack(int t)
{
	//叶子节点，输出结果
	if(t>N-1) 
	{
		//如果找到了一个更优的解
		if(CurValue>BestValue)
		{
			//保存更优的值和解
			BestValue = CurValue;
			for(int i=0;i<N;++i) BestX[i] = x[i];
		}
	}
	else
	{
		//遍历当前节点的子节点：0 不放入背包，1放入背包
		for(int i=0;i<=1;++i)
		{
			x[t]=i;
 
			if(i==0) //不放入背包
			{
				backtrack(t+1);
			}
			else //放入背包
			{
 				//约束条件：放的下
				if((CurWeight+w[t])<=C)
				{
					CurWeight += w[t];
					CurValue += v[t];
					backtrack(t+1);
					CurWeight -= w[t];
					CurValue -= v[t];
				}
			}
		}
		//PS:上述代码为了更符合递归回溯的范式，并不够简洁
	}
}
 
int main(int argc, char* argv[])
{
	backtrack(0);
 
	printf("最优值：%d\n",BestValue);
 
	for(int i=0;i<N;i++)
	{
	   printf("最优解：%-3d",BestX[i]);
	}
	return 0;
}
