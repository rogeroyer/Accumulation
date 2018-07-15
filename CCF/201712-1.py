'''
@author:roger
Q:最小差值
Addr:http://118.190.20.162/view.page?gpid=T68
'''

length = int(input())
array_input = list(map(int, input().split()))

array_input = sorted(array_input)

result = array_input[1] - array_input[0]
for index in range(1, len(array_input) - 1, 1):
    temp = array_input[index + 1] - array_input[index]
    if temp < result:
        result = temp

print(result)
