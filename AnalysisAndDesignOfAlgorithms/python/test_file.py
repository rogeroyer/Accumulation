#coding=utf-8


from dynamicProcess import dynamicPrograming
from package_memory import package_memory_deal
import pandas as pd
import numpy as np
import time

dataSet = pd.read_csv(r'weight.csv', nrows=29)
weight = list(dataSet['weight'])
value = list(dataSet['value'])
# print(sum(weight))
# print(value)
max_weight = 4500

# 14737
# 用时： 1.0313220493257882


# weight = [0, 19, 23, 12, 34, 24, 34, 56, 24, 53, 35]
# value = [0, 57, 68, 87, 17, 12,  21, 31, 42, 14, 15]
# max_weight = 300

start = time.clock()
al = package_memory_deal(weight, value, max_weight, printMatrix=True)
al.print_out()
timeused = time.clock() - start
print('用时：', timeused)

start = time.clock()
al = dynamicPrograming(weight, value, max_weight)
al.printout()
timeused = time.clock() - start
print('用时：', timeused)


