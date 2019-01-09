"""
Function:一个函数可以有多个参数，在有些情况下有的参数可以先得到，而有的参数需要在后面的情景中才能知道。
Python提供了partial函数用于携带部分参数生成一个新函数。
"""

>>> def add(a, b):
...     return a + b
...
>>> add(4, 1)
5
>>> functools.partial(add, 3)
functools.partial(<function add at 0x000001AD409481E0>, 3)
>>> plus = functools.partial(add, 3)
>>> plus(5)
8
