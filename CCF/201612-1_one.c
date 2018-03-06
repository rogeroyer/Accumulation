#include <stdio.h>
#include <stdlib.h>
#define N 1000
int main()
{
	int array[N];
	int n = 0, i = 0, j = 0;
	int m = 0, p = 0;
	scanf("%d", &n);
	for(i = 0;i < n;i++)
	{
		scanf("%d", &array[i]);
	}

	for(i = 0;i < n;i++)
	{
		m = 0, p = 0;
		for(j = 0;j < n;j++)
		{
			if(array[i] > array[j])
				m++;
			else if(array[i] < array[j])
				p++;
		}
		if(m == p){
			printf("%d\n", array[i]);
			exit(0);
		}
	}
	printf("-1\n");
	return 0;
}
