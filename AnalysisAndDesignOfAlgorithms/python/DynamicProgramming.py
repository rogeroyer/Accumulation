#coding=utf-8

class dynamicPrograming(object):
    def __init__(self, weight, value, max_weight):
        self.weight = weight
        self.value = value
        self.max_weight = max_weight
        self.matrix = [[0 for i in range(self.max_weight+1)] for j in range(len(self.weight))]

    def printout(self):
        self.problem()
        for x in range(len(self.matrix)):
            print(self.matrix[x])
        print(self.solve(len(self.weight)-1, self.max_weight))


    def solve(self, i, j):
        if (j >= 0 and i == 0) or (i >= 0 and j == 0):
            return 0
        if j < self.weight[i]:
            return self.solve(i - 1, j)
        else:
            return max(self.solve(i - 1, j), self.value[i] + self.solve(i - 1, j - self.weight[i]))

    def problem(self):
        for i in range(len(self.weight)):
            for j in range(self.max_weight+1):
                self.matrix[i][j] = self.solve(i, j)

# weight = [0, 19, 23, 12, 34, 24, 34, 56, 24, 53, 35]
# value = [0, 57, 68, 87, 17, 12,  21, 31, 42, 14, 15]
# max_weight = 300

weight = [0, 2, 1, 3, 2]
value = [0, 12, 10, 20, 15]
max_weight = 5

al = dynamicPrograming(weight, value, max_weight)
al.printout()
