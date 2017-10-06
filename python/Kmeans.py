#coding=utf-8

""" K-means algorithm """

import math
import random
"""数据集"""
dataSet = [[1.658985,4.285136], 
        [-3.453687,3.424321], 
        [4.838138, -1.151539], 
        [-5.379713, -3.362104], 
        [0.972564, 2.924086], 
        [-3.567919, 1.531611], 
        [0.450614, -3.302219], 
        [-3.487105, -1.724432], 
        [2.668759, 1.594842], 
        [-3.156485, 3.191137], 
        [3.165506, -3.999838], 
        [-2.786837, -3.099354], 
        [4.208187, 2.984927], 
        [-2.123337, 2.943366], 
        [0.704199, -0.479481], 
        [-0.392370, -3.963704],
        [2.831667, 1.574018],
        [-0.790153, 3.343144],  
        [2.943496, -3.357075],  
        [-3.195883, -2.283926],  
        [2.336445, 2.875106],  
        [-1.786345, 2.554248],  
        [2.190101, -1.906020],  
        [-3.403367, -2.778288],  
        [1.778124, 3.880832],  
        [-1.688346, 2.230267],  
        [2.592976, -2.054368],  
        [-4.007257, -3.207066],  
        [2.257734, 3.387564],  
        [-2.679011, 0.785119]]

def CalDistance(ListOne, ListTwo):
    """
            欧式距离计算公式
    ListOne，ListTwo -向量
    """
    if len(ListOne) != len(ListTwo):
        print "Input Error."
        exit(0)
    Length = len(ListOne)
    Sum = 0
    for i in range(Length):
        Sum += pow(ListOne[i] - ListTwo[i], 2)
    return math.sqrt(Sum)

def CenterPoint(List):
    """
            计算中心向量并返回
    """
    L = [0] * len(List[0])
    for indexOfList in range(len(List)):
        for indexOfL in range(len(L)):
            L[indexOfL] += List[indexOfList][indexOfL] 
    for indexOfL in range(len(L)):
        L[indexOfL] = 1.0 * L[indexOfL] / len(List)
    return L

def MininDegreeOfInsideClass(dataSet, k):
    """
    K-means类内分散度
    """
    W = 0.0
    for index in range(k):
        Sum = 0.0
        for i in range(len(dataSet[index])):
            Sum += pow(CalDistance(dataSet[index][i],CenterPoint(dataSet[index])), 2)
        W += Sum * len(dataSet[index])
    return W
    
def SeparateDataSet(dataSet, k):
    """
            对初始数据集进行分组
    """
    List = [[] for x in range(k)]
#     print List
    L = random.sample(dataSet, k)
    for data in dataSet:
        Max = CalDistance(data, L[0])
        flag = 0
        for index in range(1,k):
            if CalDistance(data, L[index]) < Max:
                Max = CalDistance(data, L[index])
                flag = index
        List[flag].append(data)
    return List

def CalIterative(dataSet, dataList, k):
    """ 
            给数据集重新分类
    """
    L = []
    for i in range(k):
        L.append(CenterPoint(dataList[i]))
#     print L
    List = [[] for x in range(k)]
    for data in dataSet:
        Max = CalDistance(data, L[0])
        flag = 0
        for index in range(1,k):
            if CalDistance(data, L[index]) < Max:
                Max = CalDistance(data, L[index])
                flag = index
        List[flag].append(data)
    return List

def main():
    """
            主函数:接口
    """
    print 'Please input K:'
    k = input()
    List = SeparateDataSet(dataSet, k)
    Max = MininDegreeOfInsideClass(List, k)
    while True:
#         print List
        List = CalIterative(dataSet, List, k)
        Value = MininDegreeOfInsideClass(List, k)
        if Max - Value < 1:
            break
        Max = Value
        
    for x in range(len(List)):
        print x+1,'th list:',List[x]
     
if __name__ == '__main__':
    main()

