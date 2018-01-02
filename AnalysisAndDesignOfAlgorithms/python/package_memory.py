class package_memory_deal(object):
    def __init__(self, weight, value, max_weight, printMatrix=False):
        self.weight = weight  # 存储重量 #
        self.value = value    # 存储权值 #
        self.max_weight = max_weight  # 背包所能承受最大重量 #
        self.array_length = len(self.value)  # 物品个数 #
        self.select = [[-1 for i in range(self.max_weight+1)] for j in range(self.array_length)]  # 存储矩阵 #
        self.printMatrix = printMatrix  # 是否打印存储矩阵 #

        for index in range(0, self.max_weight+1):  # 初始没有物品时候，背包的价值为0 #
            self.select[0][index] = 0
        for index in range(1, self.array_length):
            self.select[index][0] = 0

    def print_out(self):
        print(self.MFKnapsack(self.array_length - 1, self.max_weight))
        if self.printMatrix is True:
            self.select = np.array(self.select)
            print(self.select)
        self.show_element()

    def MFKnapsack(self, i, j):
        '''计算存储矩阵'''
        if self.select[i][j] < 0:
            if j < self.weight[i]:
                value = self.MFKnapsack(i - 1, j)
            else:
                value = max(self.MFKnapsack(i - 1, j), self.value[i] + self.MFKnapsack(i - 1, j - self.weight[i]))
            self.select[i][j] = value
        return self.select[i][j]  # 返回最大值 #

    def show_element(self):
        '''输出被选物品'''
        remain_space = self.max_weight  # 当前背包剩余容量 #
        for i in range(self.array_length-1, 0, -1):
            if remain_space >= self.weight[i]:
                if self.select[i][remain_space] - self.select[i-1][remain_space-self.weight[i]] == self.value[i]:
                    print('item ', i, ' is selected!')
                    remain_space = remain_space - self.weight[i]

def main():
    weight = [0, 2, 1, 3, 2]
    value = [0, 12, 10, 20, 15]
    max_weight = 5

    # weight = [0, 19, 23, 12, 34, 24, 34, 56, 24, 53, 35]
    # value = [0, 57, 68, 87, 17, 12,  21, 31, 42, 14, 15]
    # max_weight = 300

    al = package_memory_deal(weight, value, max_weight, True)
    al.print_out()

if __name__ == "__main__":
    main()
