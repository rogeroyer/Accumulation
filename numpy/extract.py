"""
Extract：从数组中提取符合条件的元素
"""

arr = np.arange(10)
arrarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Define the codition, here we take MOD 3 if zero
condition = np.mod(arr, 3)==0
conditionarray([ True, False, False,  True, False, False,  True, False, False,True])

np.extract(condition, arr)
array([0, 3, 6, 9])
