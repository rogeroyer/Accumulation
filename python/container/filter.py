"""
过滤器函数：用来筛选列表中符合条件的元素。
使用filter函数首先要有一个返回值为bool类型的函数，上述的lambda x: x > 5 and x < 8 就是一个bool函数。
"""


>>> b = filter(lambda x: x > 5 and x < 8, range(10))
>>> list(b)  
[6, 7]


>>> b =[i for i in range(10) if i > 5 and i < 8]
>>> b
[6, 7]

