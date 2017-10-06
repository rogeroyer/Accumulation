#coding=utf-8
"""
基于J48的特征选择
"""
from math import log
import operator
feature = set([])  # 该list存放特征 #

def calcShannonEnt(dataSet):
    """
    输入：数据集
    输出：数据集的香农熵
    描述：计算给定数据集的香农熵；熵越大，数据集的混乱程度越大
    """
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1 # 计算每类出现的频率 #
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries # 根据大数定律，如果统计量足够，相对频率就等于概率 #
        shannonEnt -= prob * log(prob, 2) # 加入到期望值中（因为prob在[0,1]区间，log结果为负数，所以用-），最终的期望值就是香农熵 #
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    """
    输入：数据集，选择维度，选择值
    输出：划分数据集
    描述：按照给定特征划分数据集；去除选择维度中等于选择值的项
    """
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    """
    输入：数据集
    输出：最好的划分维度
    描述：选择最好的数据集划分维度
    """
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGainRatio = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        splitInfo = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
            splitInfo += -prob * log(prob, 2)
        infoGain = baseEntropy - newEntropy # 信息增益 #
        if (splitInfo == 0): #修补溢出的bug#
            continue
        infoGainRatio = infoGain / splitInfo # 信息增益比 #
        if (infoGainRatio > bestInfoGainRatio):
            bestInfoGainRatio = infoGainRatio
            bestFeature = i
    return bestFeature #返回最好的信息集维度#

def majorityCnt(classList):
    """
    输入：分类类别列表
    输出：子节点的分类
    描述：数据集已经处理了所有属性，但是类标签依然不是唯一的，
          采用多数判决的方法决定该子节点的分类
    """
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reversed=True)
    return sortedClassCount[0][0]

def createTree(dataSet, labels):
    """
    输入：数据集，特征标签
    输出：决策树
    描述：递归构建决策树，利用上述的函数
    """
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        # 类别完全相同，停止划分
        return classList[0]
    if len(dataSet[0]) == 1:
        # 遍历完所有特征时返回出现次数最多的
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    # 得到列表包括节点所有的属性值
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

# 训练集 #
def createDataSet():
    """
    outlook->  0: sunny | 1: overcast | 2: rain
    temperature-> 0: hot | 1: mild | 2: cool
    humidity-> 0: high | 1: normal
    windy-> 0: false | 1: true
    """
    dataSet = [[0, 0, 0, 0, 'N'],
               [0, 0, 0, 1, 'N'],
               [1, 0, 0, 0, 'Y'],
               [2, 1, 0, 0, 'Y'],
               [2, 2, 1, 0, 'Y'],
               [2, 2, 1, 1, 'N'],
               [1, 2, 1, 1, 'Y']]

    labels = ['outlook', 'temperature', 'humidity', 'windy']
    return dataSet, labels

# 特征选择函数 #
def SelectFeature(decisionTree, N):
    global feature  # 引用全局list #
    if N == 0:
        return 
    for index_feature in decisionTree:
        if type(index_feature) == str:
            if index_feature not in feature:
                feature.add(index_feature)
        if type(decisionTree[index_feature]).__name__ == 'dict':
            SelectFeature(decisionTree[index_feature], N - 1)

def main():
    dataSet, labels = createDataSet()
    labels_tmp = labels[:] # 备份 #
    decisionTree = createTree(dataSet, labels_tmp) # 生成决策树 #
    print 'desicionTree:\n', decisionTree
    # N表示决策树最上面N层的特征  #
    print 'Please input N:'
    N = input()
    SelectFeature(decisionTree, N)
    print 'feature:',feature    
    

if __name__ == '__main__':
    main()
    
    
# 训练集 #
"""
outlook     temperature humidity    windy
-----------------------------------------
sunny       hot         high        false   N
sunny       hot         high        true    N
overcast    hot         high        false   Y
rain        mild        high        false   Y
rain        cool        normal      false   Y
rain        cool        normal      true    N 
overcast    cool        normal      true    Y
"""

# 数据数值化 #
"""
    outlook->  0: sunny | 1: overcast | 2: rain
    temperature-> 0: hot | 1: mild | 2: cool
    humidity-> 0: high | 1: normal
    windy-> 0: false | 1: true
"""
