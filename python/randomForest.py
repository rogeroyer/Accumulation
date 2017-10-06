# coding=utf-8
# 解释器：Anaconda内置python，包含sklearn库 #
import random
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# 载入鸢尾草样本集
iris = load_iris()


def getDataSet():
    """
    随机获取N个数据集
    0 <= N <= 150
    """
    # iris.data 特征集
    # iris.target 分类标签集
    dataSet = np.zeros([len(iris.data), len(iris.data[0]) + 1])
    for index in range(len(iris.data)):
        for row in range(len(iris.data[0])):
            dataSet[index][row] = iris.data[index][row]
        dataSet[index][len(iris.data[0])] = iris.target[index]
    # print dataSet
    N = 100;  # 选取100个样本
    L = np.array(random.sample(dataSet, N))
    #     print 'L:',L,'length of L is:',len(L)  # just for test
    return L;


def getRandomFeature():
    """
    随机选取K个特征
    0 <= K <= 4
    """
    dataSet = getDataSet();
    K = 2;  # 选取2个样本
    List = np.arange(1, len(iris.data[0]) + 1)
    List_row = sorted(random.sample(List, K))  # 提取K个特征索引并按升序排序
    sample = np.zeros([len(dataSet), K + 1])  # 样本集
    #     print List_row # for test
    for i in range(len(dataSet)):
        for j in range(K):
            sample[i][j] = dataSet[i][List_row[j] - 1]
        sample[i][K] = dataSet[i][len(dataSet[0]) - 1]
    return sample, List_row


# sampleSet = getRandomFeature(dataSet)
# print sampleSet
# print 'length of sample is:',len(sampleSet)

def getRandomForest():
    """
    生成随机森林
    num为模型个数 && num >= 0
    """
    num = 6  # 生成4个训练模型
    module = []
    for x in range(num):
        sample, List_row = getRandomFeature()
        if x == 0:
            ListForFeature = np.array(List_row)
        else:
            List_row = np.array(List_row)
            ListForFeature = np.vstack((ListForFeature, List_row))  # 数组合成 #

        length = len(sample[0])
        data = sample[:, 0:(length - 1)]
        target = sample[:, (length - 1):(length)]
        clf = DecisionTreeClassifier()  # 调用库函数，决策树分类器 #
        clf.fit(data, target)  # 训练模型 #
        module.append(clf)
    # print ListForFeature # for test
    return module, ListForFeature


def Forecast(testSet):
    module, ListForFeature = getRandomForest()
    #     print module #for test
    for index in range(len(module)):
        List_data = np.zeros(len(ListForFeature[0]))
        data = ListForFeature[index]
        for x in range(len(data)):
            List_data[x] = testSet[data[x] - 1]
        # print List_data #for test
        predicted = module[index].predict(List_data)
        if index == 0:
            predictedSet = predicted
        else:
            predictedSet = np.vstack((predictedSet, predicted))

            #     print predictedSet # for test
    result = dict()  # 收集投票结果 #
    for index in predictedSet:
        if index not in result.keys():
            result[index[0]] = 0
        result[index[0]] += 1
    max_value = max(result.values())
    print 'The result of vote:', result
    for key in result.keys():
        if result[key] == max_value:
            print 'The dataSet belong to class:', key


def main():
    testSet = np.array([5.1, 4.5, 1.7, 1.5]) # 测试数据 #
    Forecast(testSet)

# 主函数：程序入口 #
if __name__ == '__main__':
    main()

    # 供测试使用的一些数据，前四列是特征，最后一列是类别 #
    #  [ 6.7  2.5  5.8  1.8  2. ]
    #  [ 5.5  2.6  4.4  1.2  1. ]
    #  [ 5.7  2.5  5.   2.   2. ]
    #  [ 5.5  2.3  4.   1.3  1. ]
    #  [ 5.1  3.3  1.7  0.5  0. ]
    #  [ 7.1  3.   5.9  2.1  2. ]
    #  [ 6.4  2.9  4.3  1.3  1. ]
