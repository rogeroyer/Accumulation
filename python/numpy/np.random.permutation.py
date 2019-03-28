"""
Function:Randomly permute a sequence, or return a permuted range. (permute：置换)
"""

Example:

>>> import numpy as np
>>> np.random.permutation(10)
array([1, 0, 3, 8, 6, 7, 5, 2, 4, 9])
>>> np.random.permutation([1, 4, 9, 12, 15])
array([15, 12,  4,  9,  1])
>>> arr = np.arange(9).reshape((3, 3))
>>> arr
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
>>> np.random.permutation(arr)
array([[6, 7, 8],
       [0, 1, 2],
       [3, 4, 5]])
