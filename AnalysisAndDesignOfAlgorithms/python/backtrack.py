# -*- encoding: utf-8 -*-
import numpy as np
import pandas as pd
import time

dataSet = pd.read_csv(r'data.csv', nrows=20)
weight = list(dataSet['weight'])
value = list(dataSet['value'])

# weight = [191, 259, 321, 195, 332, 298, 337, 341, 368, 209, 279, 37, 143, 289, 137, 127, 213, 117, 287, 102, 278, 89, 66, 291, 238, 354, 236, 74, 199, 97, 183, 381, 253, 296, 343, 50, 267, 363, 179, 302, 212, 195, 410, 239, 122, 150, 40, 244, 296, 272, 417, 226, 352, 206, 275, 216, 19, 143, 250, 298, 274, 396, 76, 165, 253, 222, 115, 328, 378, 371, 252, 230, 198, 311, 225, 200, 104, 195, 162, 175, 223, 269, 40, 278, 190, 329, 83, 399, 211, 86, 84, 307, 196, 344, 407, 394, 278, 174, 187, 354]
# value = [201, 59, 133, 263, 223, 268, 192, 271, 386, 303, 140, 184, 310, 343, 181, 324, 264, 162, 137, 200, 286, 280, 383, 337, 172, 258, 219, 261, 188, 214, 213, 172, 71, 155, 330, 44, 183, 227, 407, 48, 193, 206, 275, 298, 372, 144, 300, 192, 161, 183, 214, 95, 326, 275, 409, 101, 255, 190, 266, 188, 263, 301, 204, 61, 215, 54, 125, 165, 115, 346, 381, 257, 219, 178, 381, 225, 378, 178, 230, 102, 139, 95, 236, 221, 240, 220, 96, 121, 269, 309, 273, 200, 188, 296, 279, 318, 200, 190, 310, 234]
# weight = weight[:25]
# value = value[:25]

start = time.clock()

nowvalue = 0
nowweight = 0
maxweight = 4500
maxvalue = 0

N = len(weight)
bag_list = np.zeros(N)
bestbag = []

def backtrack(t, nowweight):
    global nowvalue
    global maxvalue
    global bestbag

    #终止条件
    if t > N-1:
        if nowvalue > maxvalue:
            maxvalue = nowvalue
            bestbag = bag_list.copy()

    #迭代过程
    else:
        for i in range(2):
            bag_list[t] = i
            if i == 1:
                if (weight[t] + nowweight) <= maxweight:
                    nowweight = weight[t] + nowweight
                    nowvalue = value[t] + nowvalue
                    backtrack(t+1, nowweight)
                    nowweight = nowweight - weight[t]
                    nowvalue = nowvalue - value[t]
            else:
                backtrack(t+1, nowweight)


backtrack(0, 0)
timeused = time.clock() - start
print('用时：', timeused)

print("最优价值: ", maxvalue)
print("bestbag: ", bestbag)
