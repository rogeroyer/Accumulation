"""
Function:lambda的一般形式是在关键字lambda后面跟一个或多个参数，之后再紧跟一个冒号，接下来是一个表达式。
lambda是一个表达式而不是一个语句，它能够出现在python语法不允许def出现的地方。作为表达式，lambda返回一个值
（即一个新的函数）。lambda用来编写简单的函数，而def用来处理更强大的任务。
"""

Example:
>>> fun = lambda x,y : x + y
>>> print('fun(2,3)=', fun(2,3))
fun(2,3)= 5
