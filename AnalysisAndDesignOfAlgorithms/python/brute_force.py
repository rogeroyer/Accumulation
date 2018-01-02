# -*- encoding: utf-8 -*-

import numpy as np
import pandas as pd
import time

bag = pd.read_csv(r'data.csv', nrows=10)
# print(bag)
weight = bag['weight']
value = bag['value']
# weight = weight[:10]
# value = value[:10]

start = time.clock()

nowvalue = 0
nowweight = 0
maxweight = 500
maxvalue = 0

N = len(weight)
bag_list = []
bestvalue = []
bestweight = []


v = np.array(value)
w = np.array(weight)
for i in range(2**N):
    e = list(bin(i))[2:]  # 强制转换为二进制 #
    e = np.array(e) == '1'
    # print(type(len(e)))
    # print(w[N-len(e):][e])
    if sum(w[N-len(e):][e]) < maxweight:
        if sum(v[N-len(e):][e]) > maxvalue:
            maxvalue = sum(v[N-len(e):][e])
            bestvalue = v[N - len(e):][e].copy()
            bestweight = w[N - len(e):][e].copy()
            bag_list = e

bag_list = [1 if i == True else 0 for i in bag_list]
print(bestweight, bestvalue, bag_list)
timeused = time.clock() - start
print('用时：', timeused)



# backtrack(0, 0)
# print("最优价值: ", maxvalue)
# print("bestbag: ", bestbag)
