// 打酱油
#include <stdio.h>
int main()
{
	int N = 0;
	int a = 0,b = 0, c= 0;
	scanf("%d", &N);
	N /= 10;
	while(N != 0)
	{
		if(N >= 5)
		{
			a++;
			N -= 5;
		}
		else if(N >= 3)
		{
			b++;
			N -= 3;
		}
		else
		{
			c++;
			N -= 1;
		}
	}
	printf("%d\n", (7*a + 4*b + c));
	return 0;
}
