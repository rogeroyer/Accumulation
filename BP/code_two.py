# coding = utf-8
import math
import random

__author__ = "clogos"

'''Sigmoid函数及它的导数(deriv为真时为导数)'''


def sigmoid(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    else:
        return 1.0 / (1.0 + math.exp(-x))


'''定义BP网络的能量函数(误差函数)'''


def get_E(A, B, n):
    Ep = 0
    for i in range(n):
        Ep += 0.5 * ((A[i] - B[i]) ** 2)
    return Ep


'''生成[a, b]之间的随机数'''


def rand(a, b):
    return random.uniform(a, b)


'''构造一个n * m的矩阵，并用fill填充'''


def creatMatrix(n, m, fill=0.0):
    mat = []
    for i in range(n):
        mat.append([fill] * m)
    return mat


class BP:
    '''初始化BP神经网络'''

    def __init__(self, I, J, K):
        '''输入层、隐含层、输出层的单元数分别是I、J和K'''
        self.nI = I
        self.nJ = J
        self.nK = K

        '''激活三层BP神经网络结构的所有节点'''
        self.nodeI = [1.0] * self.nI
        self.nodeJ = [1.0] * self.nJ
        self.nodeK = [1.0] * self.nK

        '''构建神经元权重'''
        self.Wij = creatMatrix(self.nI, self.nJ)
        self.Wjk = creatMatrix(self.nJ, self.nK)

        '''构建权重修正矩阵'''
        self.Cij = creatMatrix(self.nI, self.nJ)
        self.Cjk = creatMatrix(self.nJ, self.nK)

        '''权重初始化'''
        for i in range(self.nI):
            for j in range(self.nJ):
                self.Wij[i][j] = rand(0.1, 0.5)
        for j in range(self.nJ):
            for k in range(self.nK):
                self.Wjk[j][k] = rand(0.1, 0.5)

    '''第一阶段，正向传播'''

    def predict(self, inputs):
        '''激活输入层'''
        for i in range(self.nI):
            self.nodeI[i] = inputs[i]

        '''激活隐含层'''
        for j in range(self.nJ):
            sumNet = 0.0
            for i in range(self.nI):
                sumNet += self.Wij[i][j] * self.nodeI[i]
            self.nodeJ[j] = sigmoid(sumNet)

        '''激活输出层'''
        for k in range(self.nK):
            sumNet = 0
            for j in range(self.nJ):
                sumNet += self.Wjk[j][k] * self.nodeJ[j]
            self.nodeK[k] = sigmoid(sumNet)

        return self.nodeK[:]

    '''第二阶段，反向传播'''

    def backPropagate(self, targets, studySpeed, correct):
        '''计算输出层的误差'''
        output_deltas = [0.0] * self.nK
        for k in range(self.nK):
            diff = targets[k] - self.nodeK[k]
            output_deltas[k] = sigmoid(self.nodeK[k], True) * diff

        '''计算隐含层的误差'''
        hidden_deltas = [0.0] * self.nJ
        for j in range(self.nJ):
            diff = 0.0
            for k in range(self.nK):
                diff += output_deltas[k] * self.Wjk[j][k]
            hidden_deltas[j] = sigmoid(self.nodeJ[j], True) * diff

        '''修正输出层与隐含层之间的权重'''
        for j in range(self.nJ):
            for k in range(self.nK):
                dtW = output_deltas[k] * self.nodeJ[j]
                self.Wjk[j][k] += studySpeed * dtW
                #				self.Wjk[j][k] += self.Cjk[j][k] * correct #考虑纠正率
                self.Cjk[j][k] = dtW

        '''修正隐含层与输入层之间的权重'''
        for i in range(self.nI):
            for j in range(self.nJ):
                dtW = hidden_deltas[j] * self.nodeI[i]
                self.Wij[i][j] += studySpeed * dtW
                #				self.Wij[i][j] += self.Cij[i][j] * correct #考虑纠正率
                self.Cij[i][j] = dtW

        '''返回误差'''
        return get_E(targets, self.nodeK, self.nK)

    def train(self, patterns, iterations=10000, studySpeed=0.5, correct=0.1, minx=0.0001):
        for i in range(iterations):
            nowError = 0.0
            for item in patterns:
                inputs = item[0]
                targets = item[1]
                self.predict(inputs)
                nowError += self.backPropagate(targets, studySpeed, correct)
            '''满足精度要求，终止学习'''
            if (nowError < minx):
                break

    def test(self, patterns):
        testResult = []
        for item in patterns:
            result = self.predict(item[0])
            #			print(item[0], '->', result, "[target]", item[1][0], "[error]", (item[1][0] - result[0]))
            testResult.append([item[0], result])
        return testResult[:]


'''拟合的函数'''


def functionF(x):
    if (x <= 1):
        return 0.5 + (0.5 / 1) * x
    elif (x <= 3):
        return 1.5 + (-1.0 / 2) * x
    else:
        return -1.5 + (0.5 / 1) * x


'''获取训练样本'''


def getTrainPattern(n, dt):
    patterns = []
    x = 0.0
    for i in range(n):
        y = functionF(x)
        patterns.append([[x], [y]])
        x += dt
    return patterns


'''获取测试样本'''


def getTestPattern(n):
    patterns = []
    for i in range(n):
        x = rand(0, 4)
        y = functionF(x)
        patterns.append([[x], [y]])
    return patterns


import numpy as np
import matplotlib.pyplot as plt

'''把最终结果作图显示'''


def Drawing(trainPatterns, testPatterns):
    testPatterns.sort()
    xData1 = []
    yData1 = []
    for x in trainPatterns:
        xData1.extend(x[0])
        yData1.extend(x[1])
    xData1 = np.array(xData1)
    yData1 = np.array(yData1)
    xData2 = []
    yData2 = []
    for x in testPatterns:
        xData2.extend(x[0])
        yData2.extend(x[1])
    xData2 = np.array(xData2)
    yData2 = np.array(yData2)

    plt.figure(num=1, figsize=(8, 6))
    plt.title('BP', size=14)
    plt.xlabel('x-axis', size=14)
    plt.ylabel('y-axis', size=14)
    plt.plot(xData1, yData1, color='b', linestyle='-', label='trainPatterns')
    plt.plot(xData2, yData2, color='r', linestyle='--', marker='o', label='testResult')
    plt.legend(loc='upper left')
    plt.savefig('BP.png', format='png')


def main():
    trainPatterns = getTrainPattern(80, 0.05)
    testPatterns = getTestPattern(100)
    bp = BP(1, 10, 1)
    bp.train(trainPatterns)
    testResult = bp.test(testPatterns)

    Drawing(trainPatterns, testResult)


if __name__ == "__main__":
    main()
