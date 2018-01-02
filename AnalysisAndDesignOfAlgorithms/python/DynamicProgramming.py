#coding=utf-8

'''
算法描述：动态规划算法，只求最大值不保存中间过程
性能分析：时间复杂度较高，达到2的n次方
编译环境：python3.0以上
'''

class dynamicPrograming(object):
    def __init__(self, weight, value, max_weight, printMatrix=False):
        self.weight = weight  # 存储重量 #
        self.value = value    # 存储权值 #
        self.max_weight = max_weight   # 背包所能承受最大重量 #
        self.printMatrix = printMatrix  # 是否打印存储矩阵 #
        self.matrix = []

    def printout(self):
        if self.printMatrix is True:
            self.matrix = [[0 for i in range(self.max_weight + 1)] for j in range(len(self.weight))]
            self.problem()
            for x in range(len(self.matrix)):
                print(self.matrix[x])
        print(self.solve(len(self.weight)-1, self.max_weight))

    def solve(self, i, j):
        '''求最大价值'''
        if (j >= 0 and i == 0) or (i >= 0 and j == 0):  # 终止条件 #
            return 0
        if j < self.weight[i]:
            return self.solve(i - 1, j)   # 不选上该物品 #
        else:
            return max(self.solve(i - 1, j), self.value[i] + self.solve(i - 1, j - self.weight[i]))  # 选上该物品 #

    def problem(self):
        '''计算存储矩阵'''
        for i in range(len(self.weight)):
            for j in range(self.max_weight+1):
                self.matrix[i][j] = self.solve(i, j)

def main():
    # weight = [0, 19, 23, 12, 34, 24, 34, 56, 24, 53, 35]
    # value = [0, 57, 68, 87, 17, 12,  21, 31, 42, 14, 15]
    # max_weight = 300

    weight = [0, 2, 1, 3, 2]
    value = [0, 12, 10, 20, 15]
    max_weight = 5

    al = dynamicPrograming(weight, value, max_weight, True)
    al.printout()

if __name__ == "__main__":
    main()

