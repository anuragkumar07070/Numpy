# shape of an array is the no. of element in each dimension

import numpy as np
arr = np.array([[1,2,3,4],[9,5,6,8]])
print(arr.shape) # (row,col)

three_dim = np.array([[[1,2,33,4],[1,2,3,2]],[[1,7,4,32],[3,4,36,3]]])
print(three_dim.shape) 
print(three_dim) # (two array, 2 rows in array, 4 columns in array)

ten_dim = np.array([1,23,42,63,54],ndmin=10)
print(ten_dim)
print(ten_dim.shape)