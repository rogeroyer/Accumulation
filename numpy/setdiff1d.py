"""
setdiff1d：如何找到仅在 A 数组中有而 B 数组没有的元素
"""

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array([3,4,7,6,7,8,11,12,14])
c = np.setdiff1d(a,b)
carray([1, 2, 5, 9])

