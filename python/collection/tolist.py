
>>> from numpy import *
>>> a1 = [[1,2,3],[4,5,6]] #列表
>>> a2 = array(a1) #数组
>>> a2
array([[1, 2, 3],
       [4, 5, 6]])
>>> a3 = mat(a1) #矩阵
>>> a3
matrix([[1, 2, 3],
        [4, 5, 6]])
>>> a4 = a2.tolist()
>>> a4
[[1, 2, 3], [4, 5, 6]]
>>> a5 = a3.tolist()
>>> a5
[[1, 2, 3], [4, 5, 6]]
>>> a4 == a5
True




>>> a1=[1,2,3]   #列表
>>> a2=array(a1)
>>> a2
array([1, 2, 3])
>>> a3=mat(a1)
>>> a3
matrix([[1, 2, 3]])
>>> a4=a2.tolist()
>>> a4
[1, 2, 3]
>>> a5=a3.tolist()
>>> a5
[[1, 2, 3]]
>>> a6=(a4==a5)
>>> a6
False
>>> a7=(a4 is a5[0])
>>> a7
False
