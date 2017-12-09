#coding=utf-8

import numpy as np
import math

'''sigmoid激活函数'''
def sigmoid(x):
    return 1.0 / (1 + math.exp(-x))

'''BP算法'''
class BPalgorithm(object):
    def __init__(self, layer, number, train_data, label_data, learning_rate = 0.1):
        self.layer = layer  #隐藏神经元层数#
        self.number = number  #隐藏层每一层神经元的个数#
        self.train_data = train_data  #训练集#
        self.input_neuron_num = len(self.train_data[0])  #输入神经元个数#
        self.label_data = label_data  #训练标签#
        self.output_neuron_num = len(self.label_data[0])  #输出神经元个数#
        self.hide_threshold = [[0 for i in range(self.layer)] for index in range(self.number)]  #各隐层神经元的阈值#
        self.output_threshold = [0 for j in range(self.output_neuron_num)]  #输出层各神经元的阈值#
        self.v = [[0 for i in range(self.number)] for j in range(self.input_neuron_num)]  #输入层神经元和隐层神经元的连接权值#
        # self.v = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1]]
        self.w = [[[0 for i in range(self.number)] for j in range(self.number)] for k in range(self.layer - 1)]  #隐层神经元和隐层神经元之间的连接权值#
        self.u = [[0 for i in range(self.output_neuron_num)] for j in range(self.number)]   #y最后一个隐层神经元和输出神经元之间的连接权值#
        self.learning_rate = learning_rate

    def printout(self):
        print('v:', self.v)
        print('w:', self.w)
        print('u:', self.u)
        # print('hide_threshold:', self.hide_threshold)
        # print('output_threshold:', self.output_threshold)
        # print('layer:', self.layer)
        # print('train_data:', self.train_data)
        # print('label_data:', self.label_data)

    def get_result(self, input, index):
        net = []
        result = []
        for i in range(self.number):
            get = 0
            for j in range(self.number):
                get += (self.w[index][j][i] * input[j])
            get -= self.hide_threshold[i][index + 1]
            net.append(get)
            result.append(sigmoid(get))
        return result, net

    '''预测结果'''
    def predict(self, input_data):
        '''计算第一隐层输出'''
        self.fin_result = []  #存放各层神经元最终的输出#
        self.net = []  #存放各层神经元的输入net#
        result = []
        net_one = []
        for i in range(self.number):
            get = 0
            for j in range(self.input_neuron_num):
                get += (self.v[j][i] * input_data[j])
            get -= self.hide_threshold[i][0]
            net_one.append(get)
            result.append(sigmoid(get))

        self.fin_result.append(result)
        self.net.append(net_one)
        '''计算到最后一个隐层输出为止'''
        for index in range(self.layer - 1):
            # net_one = []
            result, net_one = self.get_result(result, index)
            self.fin_result.append(result)
            self.net.append(net_one)

        '''计算最后一个隐层到输出层的结果'''
        self.finally_result = []
        self.finally_net = []
        net_one = []
        for i in range(self.output_neuron_num):
            get = 0
            for j in range(self.number):
                get += (self.u[j][i] * result[j])
            get -= self.output_threshold[i]
            self.finally_net.append(get)
            self.finally_result.append(sigmoid(get))

        self.net.append(self.finally_net)
        self.fin_result.append(self.finally_result)
        # print('fin_result', self.fin_result)
        # print('net', self.net)
        return self.finally_result

    def cal_E(self):
        '''获取能量误差'''
        y = self.predict(self.train_data)
        result = 0
        for index in range(self.output_neuron_num):
            result += (y[index] - self.label_data[index])**2
        result /= 2
        # print(result)
        return result

    '''计算局部梯度'''
    def get_part_tidu(self, net, index):
        result_part_tidu = []
        for y in range(self.number):
            part_tidu = 0
            for x in range(len(net)):
                part_tidu += self.net_list[x] * self.w[index][y][x]
            result_part_tidu.append(part_tidu)
        self.net_list = result_part_tidu
        return self.net_list

    '''修改权值'''
    def modify_weight(self):
        '''首先更改最后一个隐层的权值'''
        self.net_list = []
        for i in range(self.output_neuron_num):
            o = sigmoid(self.finally_net[i])
            net = -(self.label_data[i] - self.finally_result[i]) * o * (1 - o)
            self.net_list.append(net)
            for j in range(self.number):
                self.u[j][i] += self.learning_rate * (-net)

        '''更新隐层神经元的权值'''

        result_part_tidu = []
        for y in range(self.number):
            part_tidu = 0
            for x in range(len(self.net_list)):
                part_tidu += self.net_list[x] * self.u[y][x]
            result_part_tidu.append(part_tidu)
        self.net_list = result_part_tidu

        index = self.layer - 2
        while index >= 0:
            for i in range(self.number):
                for j in range(self.number):
                    o = sigmoid(self.net[index+1][i])
                    self.w[index][j][i] += (self.learning_rate * o * (1 - o) * self.fin_result[index][i] * self.net_list[i])
            self.net_list = self.get_part_tidu(self.net_list, index)
            index -= 1

        '''更改输入层神经元的权值'''
        for i in range(self.number):
            for j in range(self.input_neuron_num):
                o = sigmoid(self.net[0][i])
                self.v[j][i] += self.learning_rate * o * (1 - o) * self.train_data[j] * self.net_list[i]

    def train_module(self):
        train_data = self.train_data
        label_data = self.label_data
        for count in range(10000):
            e = 0
            for index in range(len(train_data)):
                self.train_data = train_data[index]
                # print self.train_data
                self.label_data = label_data[index]
                self.predict(self.train_data)
                self.modify_weight()
            # self.printout()
                e += self.cal_E()
            print e/len(train_data)

# List = [[1 for i in range(5)] for index in range(5)]
# train_data = []
# label_data = []
# for index in range(8):
#     data = list(np.random.rand(5))
#     label = list(np.random.rand(4))
#     train_data.append(data)
#     label_data.append(label)

train_data = [[1,2,6],[4,5,6,3],[2,5,1,1],[4,5,8,8]]
label_data = [[1,-1,1],[-1,1,1],[-1,-1,1],[1,1,1]]
# train_data = [[1,1,1],[1,-1,1],[1,1,-1],[-1,-1,-1]]
# label_data = [[1],[1],[1],[-1]]

layer = 3   #隐藏神经元层数#
number = 5   #隐藏层每一层神经元的个数#
learning_rate = 0.1   #学习率#
bp = BPalgorithm(3, 5, train_data, label_data, learning_rate)
bp.train_module()


# label_data = [[[1, 1, -1, 1, -1],[1, 1, -1, 1, -1]],[[1, 1, -1, 1, -1],[1, 1, -1, 1, -1]]]
# print label_data[0][0][2]
