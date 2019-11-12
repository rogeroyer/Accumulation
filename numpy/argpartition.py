array = np.array([10, 7, 4, 3, 2, 2, 5, 9, 0, 4, 6, 0])
index = np.argpartition*(array, -5)[-5:]

index
array([ 6,  1, 10,  7,  0], dtype=int64)

np.sort(array[index])
array([ 5,  6,  7,  9, 10])
