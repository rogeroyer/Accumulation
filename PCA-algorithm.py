#coding=utf-8
##########################
#     PCA algorithm      #
#    Writed by:roger     #
##########################

import numpy as np
from numpy import *

dataSet = [[5.1, 3.5, 1.4, 0.2],
            [4.9, 3.0, 1.4, 0.2],
            [4.7, 3.2, 1.3, 0.2],
            [4.6, 3.1, 1.5, 0.2],
            [5.0, 3.6, 1.4, 0.2],
            [5.4, 3.9, 1.7, 0.4],
            [4.6, 3.4, 1.4, 0.3],
            [5.0, 3.4, 1.5, 0.2],
            [4.4, 2.9, 1.4, 0.2],
            [4.9, 3.1, 1.5, 0.1],
            [5.4, 3.7, 1.5, 0.2],
            [4.8, 3.4, 1.6, 0.2],
            [4.8, 3.0, 1.4, 0.1],
            [4.3, 3.0, 1.1, 0.1],
            [5.8, 4.0, 1.2, 0.2],
            [5.7, 4.4, 1.5, 0.4],
            [5.4, 3.9, 1.3, 0.4],
            [5.1, 3.5, 1.4, 0.3],
            [5.7, 3.8, 1.7, 0.3],
            [5.1, 3.8, 1.5, 0.3],
            [5.4, 3.4, 1.7, 0.2],
            [5.1, 3.7, 1.5, 0.4],
            [4.6, 3.6, 1.0, 0.2],
            [5.1, 3.3, 1.7, 0.5],
            [4.8, 3.4, 1.9, 0.2],
            [5.0, 3.0, 1.6, 0.2],
            [5.0, 3.4, 1.6, 0.4],
            [5.2, 3.5, 1.5, 0.2],
            [5.2, 3.4, 1.4, 0.2],
            [4.7, 3.2, 1.6, 0.2]]

####### 矩阵转置 #######
def MatrixT(L):
    L1 = [([0] * len(L)) for i in range(len(L[0]))]
    for x in range(0, len(L)):
        for y in range(0, len(L[x])):
            L1[y][x] = L[x][y]
    return L1

######### 矩阵相乘 ##########
def MultiplyMatrix(ListOne, ListTwo):
    List = [[0] * len(ListTwo[0]) for i in range(len(ListOne))]
    for x in range(0, len(ListOne)):
        for y in range(0, len(ListTwo[0])):
            for z in range(0, len(ListTwo)):
                List[x][y] += ( ListOne[x][z] * ListTwo[z][y] )
    return List

######## 每个向量值减去该维度上的平均值 #########
def ReduceAverage(L):
    List = []
    for i in range(0, len(L)):
        sum_row = 0.0
        for j in range(0, len(L[i])):
            sum_row = sum_row + L[i][j]
        List.append(sum_row / len(L[i]))
    for i in range(0, len(L)):
        for j in range(0, len(L[i])):
            L[i][j] = L[i][j] - List[i]
    return L

######## 协方差矩阵 ##########
def CovForX(dataSet):
    length = len(dataSet)
    L = MultiplyMatrix(dataSet, MatrixT(dataSet))
    for i in range(0, len(L)):
        for j in range(0, len(L[i])):
            L[i][j] *= (1.0 / length)
    return L

def main():
    x = MatrixT(dataSet)
    X = ReduceAverage(x) # 减去平均值的数据集 #
    Cov_X = CovForX(X) # 协方差矩阵 #
#     print Cov_X
    t, Q = np.linalg.eig(Cov_X)  # 求矩阵的特征向量Q和特征值t #
    k = 2  # 最后只保留2维特征 #
    T = argsort(t)
    T = T[:-(k+1):-1]   #保留最大的前K个特征值
    P = np.vstack((Q[T[0]], Q[T[1]]))
    Y = MultiplyMatrix(P, x) # 降维后的矩阵 #
    print Y
    
if __name__ == '__main__':
    main()
