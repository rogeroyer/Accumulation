"""
它有点像map函数，但是map函数用于逐一遍历，而reduce函数用于递归计算。
"""

>>> from functools import reduce
>>> reduce(lambda x,y: x*y, range(1, 10))
362880
>>> reduce(lambda x,y: x*y, range(1, 5))
24


"""
在2.x中reduce可以直接使用，而在3.x中reduce函数已经被移出了全局命名空间，它是被置于functools库中，如需使用，则要通过from functools import reduce 引入reduce。
"""
