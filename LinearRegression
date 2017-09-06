#coding=utf-8
import numpy as np
# 线性回归算法实现 #
# 计算转置矩阵 #
def MatrixT(L):
    L1 = np.array([([0] * len(L)) for i in range(len(L[0]))])
    # L1 = [([0] * len(L[0])) for i in range(len(L))]
    for x in range(0, len(L)):
        for y in range(0, len(L[x])):
            for y in range(0, len(L[x])):
                L1[y][x] = L[x][y]
    return L1

# 显示数组元素 #
def DisplayMatrix(L):
    for x in L:
        print x

# 矩阵相乘 #
def MultiplyMatrix(ListOne, ListTwo):
    List = np.zeros([len(ListOne), len(ListTwo[0])])
    # print List
    # print len(ListOne)
    # print len(ListTwo[0])
    for x in range(0, len(ListOne)):
        for y in range(0, len(ListTwo[0])):
            for z in range(0, len(ListTwo)):
                List[x][y] += ( ListOne[x][z] * ListTwo[z][y] )
    return List

# 逆矩阵 #
def ReverseMatrix(L):
        return np.linalg.inv(L)

# 把X和Y的矩阵传进去直接返回结果W #
def Result(X, Y):
    A = MatrixT(X)
    # print 'A:', A
    B = MultiplyMatrix(A, X)
    # print 'B:', B
    C = ReverseMatrix(B)
    # print 'C:', C
    # print C,A
    D = MultiplyMatrix(C, A)
    # print 'D:', D
    W = MultiplyMatrix(D, Y)
    return W

# print MultiplyMatrix(MultiplyMatrix(ReverseMatrix(MultiplyMatrix(MatrixT(X), X)), MatrixT(X)), Y)

# 单变量测试 Y = W0 + W1 * X#
X = np.array([[1, 2], [1, 6], [1, 9], [1, 13]])
Y = np.array([[4], [8], [12], [21]])
DisplayMatrix(Result(X, Y))

# 多变量测试 Y = W0 + W1 * X1 + W2 * X2 + W3 * X3 #
# X = np.array([[1, 2, 3, 4], [1, 6, 5, 6], [1, 9, 7, 8], [1, 13, 10, 12]])
# Y = np.array([[5], [9], [13], [25]])
# DisplayMatrix(Result(X, Y))





# coding=utf-8
# def MatrixT(L):
#     L1 = [([0] * len(L)) for i in range(len(L[0]))]
#     # L1 = [([0] * len(L[0])) for i in range(len(L))]
#     for x in range(0, len(L)):
#         for y in range(0, len(L[x])):
#             L1[y][x] = L[x][y]
#     return L1
#
#
# # 显示数组元素 #
# def DisplayMatrix(L):
#     for x in L:
#         print x
#
#
# # 矩阵相乘 #
# def MultiplyMatrix(ListOne, ListTwo):
#     #     List = np.zeros([len(ListOne), len(ListTwo[0])])
#     List = [[0] * len(ListTwo[0]) for i in range(len(ListOne))]
#     # print List
#     # print len(ListOne)
#     # print len(ListTwo[0])
#     for x in range(0, len(ListOne)):
#         for y in range(0, len(ListTwo[0])):
#             for z in range(0, len(ListTwo)):
#                 List[x][y] += (ListOne[x][z] * ListTwo[z][y])
#     return List
#
#
# # 逆矩阵 #
# def ReverseMatrix(L):
#     def DetOfList(L):
#         if len(L) == 1:
#             return L[0]
#         if len(L) == 2:
#             return L[0][0] * L[1][1] - L[0][1] * L[1][0]
#         else:
#             result = 0
#             for i in range(0, len(L[0])):
#                 List = [[row[a] for a in range(len(L)) if a != i] for row in L[1:]]
#                 result += (L[0][i] * pow(-1, i) * DetOfList(List))
#         return result
#
#     def ListForYuzishi(L):
#         List_L = [[0] * len(L[0]) for j in range(len(L))]
#         for i in range(len(L[0])):
#             for j in range(len(L)):
#                 List = [[L[b][a] for a in range(len(L[0])) if a != j] for b in range(len(L)) if b != i]
#                 List_L[i][j] = DetOfList(List)
#         return List_L
#
#     def ListForBansui(L):
#         L = ListForYuzishi(L)
#         for i in range(len(L[0])):
#             for j in range(0, i):
#                 if j < i:
#                     temp = L[i][j]
#                     L[i][j] = L[j][i] * pow(-1, i + j)
#                     L[j][i] = temp * pow(-1, i + j)
#         return L
#
#     if DetOfList(L) == 0:
#         print "The matrix hasn't reverse_matrix"
#         exit(1)
#     det = 1.0 / DetOfList(L)
#     L = ListForBansui(L)
#     for i in range(len(L[0])):
#         for j in range(len(L)):
#             L[i][j] = det * L[i][j]
#     return L
#
#
# # 把X和Y的矩阵传进去直接返回结果W #
# def Result(X, Y):
#     A = MatrixT(X)
#     #     print 'A:', A
#     B = MultiplyMatrix(A, X)
#     #     print 'B:', B
#     C = ReverseMatrix(B)
#     #     print 'C:', C
#     #     print C,A
#     D = MultiplyMatrix(C, A)
#     #     print 'D:', D
#     W = MultiplyMatrix(D, Y)
#     return W
#

# print MultiplyMatrix(MultiplyMatrix(ReverseMatrix(MultiplyMatrix(MatrixT(X), X)), MatrixT(X)), Y)

# 单变量测试 Y = W0 + W1 * X#
# X = [[1, 2], [1, 6], [1, 9], [1, 13]]
# Y = [[4], [8], [12], [21]]
# DisplayMatrix(Result(X, Y))

# 多变量测试 Y = W0 + W1 * X1 + W2 * X2 + W3 * X3 #
# X = [[1, 2, 3, 4], [1, 6, 5, 6], [1, 9, 7, 8], [1, 13, 10, 12]]
# Y = [[5], [9], [13], [25]]
# DisplayMatrix(Result(X, Y))


