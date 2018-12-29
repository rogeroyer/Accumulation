
>>> str = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a', 'b', 'c'])
>>> str
   a  b  c
0  1  2  3
1  4  5  6
2  7  8  9
>>> str.corr()
     a    b    c
a  1.0  1.0  1.0
b  1.0  1.0  1.0
c  1.0  1.0  1.0
>>> str.corr(method='pearson')    # 皮尔逊相关系数
     a    b    c
a  1.0  1.0  1.0
b  1.0  1.0  1.0
c  1.0  1.0  1.0

>>> str.corr(method='kendall')    # 肯德尔系数
     a    b    c
a  1.0  1.0  1.0
b  1.0  1.0  1.0
c  1.0  1.0  1.0
>>> s1 = str.loc[0]
>>> s2 = str.loc[1]
>>> s1
a    1
b    2
c    3
Name: 0, dtype: int64
>>> s2
a    4
b    5
c    6
Name: 1, dtype: int64
>>> s1.corr(s2, method='pearson')   # 计算s1和s2相关系数
1.0
