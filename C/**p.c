#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define M 100

int main()
{
	/*
    char num[15] = {"HelloWorld"};
	char* p = num;
	char** ptr = NULL;
	ptr = &p;
	**ptr = {"HelloWorld"};
	printf("%s\n", *num);
	printf("%s\n", *(num+1));
	*/

	/*
	int a=12;
	int b;
	int *p;
	int **ptr;
	p=&a;//&a的结果是一个指针，类型是int*，指向的类型是int，指向的地址是a的地址。
	*p=24;//*p的结果，在这里它的类型是int，它所占用的地址是p所指向的地址，显然，*p就是变量a。
	ptr=&p;//&p的结果是个指针，该指针的类型是p的类型加个*，在这里是int**。该指针所指向的类型是p的类型，这里是int*。该指针所指向的地址就是指针p自己的地址。
	*ptr=&b;//*ptr是个指针，&b的结果也是个指针，且这两个指针的类型和所指向的类型是一样的，所以?amp;b来给*ptr赋值就是毫无问题的了
	**ptr=34;//*ptr的结果是ptr所指向的东西，在这里是一个指针，对这个指针再做一次*运算，结果就是一个int类型的变量。
	printf("%d\n", b);
	*/

	char *arr[20] = {{"HelloWorld"}, {"HelloC"}};
	char **parr=arr;//如果把arr看作指针的话，arr也是指针表达式
	char *str;
	str=*parr;//*parr是指针表达式
	str=*(parr+1);//*(parr+1)是指针表达式
	str=*(parr+2);//*(parr+2)是指针表达式
	printf("%p\n", **parr);
	printf("%p\n", arr);
	puts(*arr);
	puts(*(arr+1));
	puts(*parr);
    return 0;

}
