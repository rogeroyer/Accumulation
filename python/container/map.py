

>>> a = [1, 2, 3, 4, 5]
>>> b = map(lambda x: x+2, a)
>>> b
<map object at 0x000001E21018E4E0>
>>> list(b)
[3, 4, 5, 6, 7]
>>> c = map(lambda x, y: x*y, a, b)
>>> list(c)
[3, 8, 15, 24, 35]
