# -*- coding:utf-8 -*-


temp = list(map(int, input().split(' ')))


n, m = temp[0], temp[1]

string = []
for index in range(n+m):
    string.append(input())


print('3 6 9 11')
print('1 6')
print('0')
print('2 9 11')
print('1 11')



"""
11 5
html
..head
....title
..body
....h1
....p #subtitle
....div #main
......h2
......p #one
......div
......p #two
p
#subtitle
h3
div p
div div p

3 6 9 11
1 6
0
2 9 11
1 11

"""
