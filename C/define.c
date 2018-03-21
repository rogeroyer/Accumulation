
#include<stdio.h>
#define A() n+m
#define area(x) x*x 
#define MAX( x, y) x > y ? x : y
#define conn(x,y) x##y 
int main()
{
	int m = 1, n = 2;
	char * p = conn("I", " love apple");  
	printf("%d\n",A());
	printf("%d\n",area(2+2));
	printf("%d\n",area(2+2)/area(2+2));
	printf("%d\n",MAX(5, 3));
	puts(p); 
	return 0;
}
