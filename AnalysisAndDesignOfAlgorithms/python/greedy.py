# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 20:14:59 2017

@author: administrator
"""
import pandas as pd
import time
import numpy as np

def greedy(num, cap, sorted_wv, weights, values, select, w_v):
    c = cap
    max_value = 0
    for i in range(num):
        #如果背包的容量大于比值最大的物品的重量
        if(c >= weights[sorted_wv[i]]):
            print(sorted_wv[i])
            c = c - weights[sorted_wv[i]]
            max_value += values[sorted_wv[i]]
            select[sorted_wv[i]] = 1
    print("背包的最大价值为：%d" % max_value) 
    print(select)
    show(select, weights, values, w_v)
    
def show(select, weights, values, w_v ):
    print("所选择的物体为：")
    for i in range(len(select)):
        if(select[i] == 1):
            print("第%d号物体" % i, "，其价值为%d" % values[i],"，重量为%d" % weights[i])

if __name__ == '__main__':
    start = time.clock() 
    num = 28   # 物品个数 #
    cap = 4500   # 背包最大容量 #
    select = [0 for _ in range(num)] 
    #物品的价值/重量比
    w_v = np.array([0.0 for _ in range(num)])
    #print(w_v)
    dataSet = pd.read_csv(r'data.csv', nrows=28)  # 同物品个数相同 #
    weights = list(dataSet['weight'])
    values = list(dataSet['value'])

    #weights = [10,20,30]
    #values = [60,100,120]
    for i in range(num):
        w_v[i] = values[i] / weights[i]
    # print(w_v)
    #按升序排列的价值与重量的比值
    sorted_wv = np.argsort(-w_v)
    # print(sorted_wv)
    greedy(num, cap, sorted_wv, weights, values, select, w_v)
    timeused = time.clock() - start
    print('用时：', timeused)
