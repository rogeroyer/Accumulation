# -*- coding:utf-8 -*-

num = int(input())
prices = list(map(int, input().split(' ')))

original = [0 for index in range(num)]

def check_price(one, two):
    lenght = len(one)
    if int((one[0] + one[1]) / 2) != two[0]:
        return False
    if int((one[lenght-2] + one[lenght-1]) / 2) != two[lenght-1]:
        return False
    for index in range(1, lenght - 1):
        if int((one[index-1] + one[index] + one[index+1]) / 3) != two[index]:
            return False
    return True

flag = 1
while(flag <= 100):
    original[0] = flag
    original[1] = 2 * prices[0] - original[0]

    for index in range(2, num-1):
        temp = 3 * prices[index-1] - original[index-2] - original[index-1]
        if temp > 0:
            original[index] = temp
        else:
            original[index] = 1

    original[num-1] = 2 * prices[num-1] - original[num-2]

    if check_price(original, prices) is True:
        break
    else:
        flag += 1

original = str(original).replace('[', '').replace(']', '').replace(',', '')
print(original)


"""
case one:
8
2 2 1 3 4 9 10 13

2 2 2 1 6 5 16 10
"""
