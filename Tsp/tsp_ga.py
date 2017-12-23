# -*- encoding: utf-8 -*-

import random
import math
from GA import GA
import matplotlib.pyplot as plt

class TSP(object):
    def __init__(self, aLifeCount=100, ):
        self.initCitys()
        self.lifeCount = aLifeCount
        self.ga = GA(aCrossRate=0.7,
                     aMutationRage=0.02,
                     aLifeCount=self.lifeCount,
                     aGeneLenght=len(self.citys),
                     aMatchFun=self.matchFun())

    def initCitys(self):
        self.citys = []
        """
        for i in range(34):
              x = random.randint(0, 1000)
              y = random.randint(0, 1000)
              self.citys.append((x, y))
        """

        # 47城市经纬度
        self.citys.append((6734, 1453))
        self.citys.append((2233, 10))
        self.citys.append((5530, 1424))
        self.citys.append((3082, 1644))
        self.citys.append((7608, 4458))
        self.citys.append((7573, 3716))
        self.citys.append((7265, 1268))
        self.citys.append((6898, 1885))
        self.citys.append((1112, 2049))
        self.citys.append((5468, 2606))
        self.citys.append((5989, 2873))
        self.citys.append((4706, 2674))
        self.citys.append((4612, 2035))
        self.citys.append((6347, 2683))
        self.citys.append((6107, 669))
        self.citys.append((7611, 5184))
        self.citys.append((7462, 3590))
        self.citys.append((7732, 4723))
        self.citys.append((5900, 3561))
        self.citys.append((4483, 3369))
        self.citys.append((6101, 1110))
        self.citys.append((5199, 2182))
        self.citys.append((1633, 2809))
        self.citys.append((4307, 2322))
        self.citys.append((675, 1006))
        self.citys.append((7555, 4819))
        self.citys.append((7541, 3981))
        self.citys.append((3177, 756))
        self.citys.append((7352, 4506))
        self.citys.append((7545, 2801))
        self.citys.append((3245, 3305))
        self.citys.append((6426, 3173))
        self.citys.append((4608, 1198))
        self.citys.append((23, 2216))
        self.citys.append((7248, 3779))
        self.citys.append((7762, 4595))
        self.citys.append((7392, 2244))
        self.citys.append((3484, 2829))
        self.citys.append((6271, 2135))
        self.citys.append((4985, 140))
        self.citys.append((1916, 1569))
        self.citys.append((7280, 4899))
        self.citys.append((7509, 3239))
        self.citys.append((10, 2676))
        self.citys.append((6807, 2993))
        self.citys.append((5185, 3258))
        self.citys.append((3023, 1942))

    def distance(self, order):
        distance = 0.0
        for i in range(-1, len(self.citys) - 1):  # 取到-1，因为要形成一个回路形成一个哈密顿图 #
            index1, index2 = order[i], order[i + 1]
            city1, city2 = self.citys[index1], self.citys[index2]
            distance += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)   # 欧式距离 #

            """
            R = 6371.004
            Pi = math.pi
            LatA = city1[1]
            LatB = city2[1]
            MLonA = city1[0]
            MLonB = city2[0]

            C = math.sin(LatA*Pi / 180) * math.sin(LatB * Pi / 180) + math.cos(LatA * Pi / 180) * math.cos(LatB * Pi / 180) * math.cos((MLonA - MLonB) * Pi / 180)
            D = R * math.acos(C) * Pi / 100
            distance += D
            """
        return distance

    def matchFun(self):
        return lambda life: 1.0 / self.distance(life.gene)

    def run(self, n=0):
        distance_list = []
        generate = [index for index in range(1, n + 1)]
        while n > 0:
            self.ga.next()
            distance = self.distance(self.ga.best.gene)
            distance_list.append(distance)
            print(("第%d代 : 当前最小距离%f") % (self.ga.generation, distance))
            n -= 1
        print('当前最优路线:')
        string = ''
        for index in self.ga.best.gene:
            string += str(index) + '->'
        print(string[0:len(string)-2])

        '''画图函数'''
        plt.plot(generate, distance_list)
        plt.xlabel('generation')
        plt.ylabel('distance')
        plt.title('generation--distance')
        plt.show()

def main():
    tsp = TSP()
    tsp.run(100)


if __name__ == '__main__':
    main()

# 123783.378588  1
# 117006.481096  10
# 89118.050755   100
# 52978.395838   1000
# 40297.413937   10000
