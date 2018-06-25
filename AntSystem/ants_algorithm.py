# -*- coding:utf-8 -*-

'''
Author : Roger
Date : 2018.06.24
Class ： Ants
Solution ： TSP
'''

import math
import random
import copy
import numpy as np
import pandas as pd
from Ants import Ant
import matplotlib.pyplot as plt


class AntsAlgorithm(object):
    def __init__(self, m=20, alpha=1, beta=3, rho=0.5, iterations=200):
        self.m = m                                        # m 蚂蚁个数 #
        self.Alpha = alpha                                # Alpha 表征信息素重要程度的参数 #
        self.Beta = beta                                  # Beta 表征启发式因子重要程度的参数 #
        self.Rho = rho                                    # Rho 信息素蒸发系数 #
        self.Iterations = iterations                      # 最大迭代次数 #
        self.Coordinate = self.init_citys()               # 初始化城市坐标 #
        self.CityFlag = [index for index in range(0, len(self.Coordinate), 1)]   # 城市标记 #
        self.GreedyBestPath = self.calc_greedy_path()                            # 贪心算法找到的最优解 #
        self.PheromoneMatrix = np.array([[self.m / self.GreedyBestPath] * len(self.Coordinate) for index in range(len(self.Coordinate))])     # 信息素浓度矩阵 #
        self.Ants = None                                  # 初始化蚁群 #

    def init_citys(self):
        '''城市坐标'''
        coordinate = pd.read_csv(r'CityCoordinate.csv', encoding='utf-8', low_memory=False)
        return np.array(coordinate)

    def init_ants(self):
        '''初始化蚁群：随机选择一个点作为起点'''
        ants = []
        for index in range(self.m):
            single_ant = Ant(len(self.Coordinate))
            ants.append(single_ant)
        return ants

    def calc_distance(self, one, two):
        ''' one:index1  two:index2 '''
        return math.sqrt((self.Coordinate[one][1] - self.Coordinate[two][1]) ** 2 + (self.Coordinate[one][0] - self.Coordinate[two][0]) ** 2)

    def construct_path(self):
        '''构建完整路径'''
        for ants in self.Ants:
            close_table = copy.deepcopy(self.CityFlag)
            close_table.remove(ants.origin)
            open_table = copy.deepcopy(ants.path)

            while len(open_table) < len(self.CityFlag):
                i = open_table[-1]
                distance = []
                for j in range(len(close_table)):
                    distance.append(((1.0 / self.calc_distance(i, close_table[j])) ** self.Beta) * (self.PheromoneMatrix[i][close_table[j]] ** self.Alpha))
                bound = random.uniform(0, sum(distance))

                '''轮盘赌算法'''
                flag = close_table[0]
                for index in range(len(distance)):
                    bound -= distance[index]
                    if bound <= 0:
                        flag = close_table[index]
                        break
                open_table.append(flag)
                close_table.remove(flag)

            ants.path = copy.deepcopy(open_table)

            '''计算适应度'''
            total_distance = 0
            for index in range(len(ants.path) - 1):
                total_distance += self.calc_distance(ants.path[index], ants.path[index+1])
            ants.score = total_distance + self.calc_distance(ants.path[0], ants.path[-1])
            # print(ants.path)
            # print(ants.score)
        # print('over!')

    def update_pheromone(self):
        '''更新路径上的信息素'''
        for i in range(len(ant_algorithm.Coordinate)):
            for j in range(len(ant_algorithm.Coordinate)):
                self.PheromoneMatrix[i][j] = (1 - self.Rho) * self.PheromoneMatrix[i][j]

        for ants in self.Ants:
            ants.path.append(ants.origin)    # 环路 #
            for index in range(len(ants.path) - 1):
                self.PheromoneMatrix[ants.path[index]][ants.path[index+1]] = 1.0 / ants.score              # (1 - self.Rho) * self.PheromoneMatrix[ants.path[index]][ants.path[index+1]] +  #
                self.PheromoneMatrix[ants.path[index+1]][ants.path[index]] = self.PheromoneMatrix[ants.path[index]][ants.path[index+1]]

    def calc_greedy_path(self):
        '''贪心算法得到路径并用作初始化信息素'''
        open_table = [0]
        close_table = copy.deepcopy(self.CityFlag)[1:]
        sum_distance = 0
        while len(close_table) > 0:
            i = open_table[-1]
            distance = self.calc_distance(i, close_table[0])
            flag = close_table[0]
            for j in range(1, len(close_table)):
                if distance > self.calc_distance(i, close_table[j]):
                    distance = self.calc_distance(i, close_table[j])
                    flag = close_table[j]

            sum_distance += distance
            close_table.remove(flag)
            open_table.append(flag)
        return sum_distance

    def ants_run(self):
        plot_index = []
        plot_value = []
        all_best_path = None
        for index in range(self.Iterations):
            self.Ants = self.init_ants()
            self.construct_path()
            self.update_pheromone()

            best_ant = self.Ants[0].score
            best_path = self.Ants[0].path
            for ant in self.Ants:
                if best_ant > ant.score:
                    best_ant = ant.score
                    best_path = ant.path
            print('The highest adaptation of ', index+1, 'th generation is:',  best_ant)
            print('Best path:', best_path)

            plot_index.append(index+1)
            # plot_value.append(best_ant)
            if index == 0:
                plot_value.append(best_ant)
                all_best_path = best_path
            elif index != 0 and plot_value[-1] > best_ant:
                plot_value.append(best_ant)
                all_best_path = best_path
            else:
                plot_value.append(plot_value[-1])
        print('The highest adaptation of all generations is:', min(plot_value))
        print('The best path of all generations is:', all_best_path)
        print('Program is over!')

        '''plot'''
        plt.plot(plot_index, plot_value, color='green')
        plt.xlabel('Iterations')
        plt.ylabel('Adaptation')
        plt.title('Iterations-Adaptation')
        plt.savefig('Iterations-Adaptation.png')
        plt.show()


if __name__ == '__main__':
    ant_algorithm = AntsAlgorithm(m=100, alpha=1, beta=5, rho=0.5, iterations=200)
    print(ant_algorithm.GreedyBestPath)
    ant_algorithm.ants_run()

