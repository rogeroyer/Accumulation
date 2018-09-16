# -*- coding:utf-8 -*-

num = int(input())
prices = list(map(int, input().split(' ')))

second = []

first = int((prices[0] + prices[1]) / 2)
second.append(first)

for index in range(1, num-1):
    price = int((prices[index-1] + prices[index] + prices[index+1]) / 3)
    second.append(price)

end = int((prices[num-2] + prices[num-1]) / 2)


second.append(end)
second = str(second).replace('[', '').replace(']', '').replace(',', '')
print(second)


"""
8
4 1 3 1 6 5 17 9
"""
