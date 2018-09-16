# -*- coding:utf-8 -*-

num = int(input())


hman = [[0] * 2 for i in range(num)]
wman = [[0] * 2 for i in range(num)]

for index in range(num):
    hman[index] = list(map(int, input().split(' ')))

for index in range(num):
    wman[index] = list(map(int, input().split(' ')))

count = 0
for i in range(num):
    for j in range(num):
        if wman[i][0] >= hman[j][0] and wman[i][0] < hman[j][1]:
            count += min(hman[j][1], wman[i][1]) - wman[i][0]
            
        elif wman[i][0] < hman[j][1] and wman[i][1] >= hman[j][1]:
            count += hman[j][1] - hman[j][0]
            
        elif wman[i][0] < hman[j][0] and wman[i][1] > hman[j][0] and wman[i][1] < hman[j][1]:
            count += wman[i][1] - hman[j][0]
        
                   
print(count)


# print(hman[j], wman[i], count)
# print(hman[j], wman[i], count)


"""
case one:
4
1 3
5 6
9 13
14 15
2 4
5 7
10 11
13 14

3
"""

"""
case two:
8
1 2
3 5
6 7
8 13
15 20
21 23
24 25
27 30
1 3
4 5
7 9
11 12
13 15
17 22
23 26
27 30

10
""" 

"""
case three:
3
1 2
3 4
5 6
1 5
6 7
9 10

2
"""
# 1 1 1 3 3

"""
case four:
5
1 3
5 6
9 13
14 15
18 20
2 4
5 7
10 11
13 14
17 19

4
"""

"""

"""
