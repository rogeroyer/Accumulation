# -*- coding:utf-8 -*-

# sys_in = list(map(int, input().split()))
# n, m = sys_in[0], sys_in[1]
#
# matrix = []
# for index in range(m):
#     matrix.append(list(map(int, input().split())))

n, m = 6, 7
matrix = [[1, 1, 2, 3], [1, 2, 3, 2], [0, 1, 3, 30], [0, 3, 4, 20], [0, 4, 5, 30], [1, 3, 5, 6], [1, 5, 6, 1]]


def calc_distance(route):
    distance = 0
    for j in range(len(route)):
        if matrix[route[j]][0] == 0:
            distance += matrix[route[j]][3]
        else:
            if j < len(route) - 1:
                if matrix[route[j + 1]][0] == 0:
                    pass
                else:
                    temp = 0
                    while (j < len(route)) and (matrix[route[j]][0] == 1):
                        temp += matrix[route[j]][3]
                        j += 1
                    distance += temp ** 2
                    if j == len(route):
                        break
            else:
                distance += matrix[route[j]][3] ** 2
    return distance


# print(calc_distance([0, 1, 3, 4, 6]))
# print(calc_distance([0, 1, 5, 6]))


def calc_max_distance(start, node):
    global matrix
    if start == n:
        print(node)
        print(calc_distance(node))
        # exit(0)
    for i in range(m):
        if matrix[i][1] == start:
            node.append(i)
            calc_max_distance(matrix[i][2], node)


nodes = []
calc_max_distance(start=1, node=nodes)

# print(node)

'''input
6 7
1 1 2 3
1 2 3 2
0 1 3 30
0 3 4 20
0 4 5 30
1 3 5 6
1 5 6 1
'''

     未完成。。。
