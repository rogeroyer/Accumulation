
#include<iostream>
#include<cmath>

using namespace std;

const int CMAX = 40; //背包最大容量 
const int N = 4; //物品的个数
int W[N] = {3, 1, 2, 5};//物品的重量 
int P[N] = {5, 2, 4, 10};//物品的价值 
int X[N]; //解向量
int B[N][CMAX+1]; //备忘录，记录给定n个物品装入容量为c的背包的最大价值 
int sum = 0;

int Best(int n, int c); //备忘录：自顶而下，获得给定n个物品装入容量为c的背包的最大价值 
int Best_2(int n, int c);//动态规划：自底而上，获得给定n个物品装入容量为c的背包的最大价值 
int Max(int a, int b);

int main() 
{
 	int c = 6; //背包容量 
 	
 	for (int i=0; i<N; i++)//初始化为-1，表示还没有存储该备忘录 
 	{
	 	for (int j=1; j<=c; j++)
	 	{
		 	B[i][j] = -1;
		}
	}
    
//	int bestp = Best(N-1, c); 
	int bestp = Best_2(N-1, c); 
	
	for (int i=0; i<N; i++)
 	{
	 	for (int j=1; j<=c; j++)
	 	{
		 	cout << "B[" << i << "][" << j << "] = " << B[i][j] << " ";
		}
		cout << endl; 
	}
	
	int bestw = 0;
    for (int i=N-1; i>0; i--)
	{
	 	if (B[i][c] == B[i-1][c])//不装物品i 
	 	{
	        X[i] = 0;
	    }
	    else
	    {
		 	X[i] = 1;
		 	bestw += W[i];
		 	c -= W[i];
		}
	}
	X[0] = (B[0][c] > 0) ? 1 : 0; //是否装第0个物品
	bestw += (X[0] == 0) ? 0 : W[0];
	
	cout << "背包的最大价值：" << bestp << "(" << bestw << ")" << endl;
    cout << "背包的最优解：";
    for (int i=0; i<N; i++)
	{
	 	cout << X[i] << " ";
	}
	cout << endl; 
   
    system("pause");
    return 0;
}

int Max(int a, int b)
{
 	return (a > b) ? a : b;
}

int Best(int n, int c)//备忘录：自顶而下，获得给定n个物品装入容量为c的背包的最大价值 
{
 	if (B[n][c] != -1)  //如果这个问题曾经计算过，直接返回 
 	{
		return B[n][c];
	}
	
	int bestP = 0;
	if (n == 0)//处理第0个物品，即只有一个物品 
	{
		bestP = (c >= W[n]) ? P[n] : 0;
	}
	else
	{
		bestP = Best(n-1, c); //先计算不装第n个物品的情形 
		if (c >= W[n])//如果装得下，从装和不装两者中去最大值 
		{
		    bestP = Max(bestP, Best(n-1, c-W[n])+P[n]);
		}
	}
 	
	B[n][c] = bestP;//做备忘录 
	
	cout << (++sum) << ": " << "B[" << n << "][" << c << "] = " << B[n][c] << endl;
    return bestP;
}

int Best_2(int n, int c)//动态规划：自底而上，获得给定n个物品装入容量为c的背包的最大价值 
{
	//记录第0个物品装入容量为0-c的背包的最大价值 
 	int jMax = (c < W[0]-1) ? c : W[0]-1;
	for (int j=0; j<=jMax; j++)
	{
		B[0][j] = 0;
	}
	for (int j=W[0]; j<=c; j++)
	{
		B[0][j] = P[0];
	}
	
	//记录前i(i>=1)个物品装入容量为0-c的背包的最大价值 
 	for (int i=1; i<n; i++)
	{
		jMax = (c < W[i]-1) ? c : W[i]-1;
		for (int j=0; j<=jMax; j++)
		{
			B[i][j] = B[i-1][j]; 
		}
		for (int j=W[i]; j<=c; j++)
		{
			B[i][j] = (B[i-1][j] > B[i-1][j-W[i]]+P[i]) ? B[i-1][j] : B[i-1][j-W[i]]+P[i];
		}
	}
	//第n个物品只需考虑容量为c的一种情况
	B[n][c] = B[n-1][c];
	if (c >= W[n])
	{
		B[n][c] = (B[n-1][c] > B[n-1][c-W[n]]+P[n]) ? B[n-1][c] : B[n-1][c-W[n]]+P[n];
	}
	
	return B[n][c];
}
