"""
Function: convert string to true value
"""

>>> name = "pandas"
>>> eval(name)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1, in <module>
NameError: name 'pandas' is not defined
>>> import pandas
>>> eval(name)
<module 'pandas' from 'D:\\ProgramFiles\\Anacanda3\\lib\\site-packages\\pandas\\__init__.py'>
