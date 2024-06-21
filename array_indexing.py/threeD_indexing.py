# Accessing 3D array's element
# 3D array is the combination of two 2D array

# *** 3 step to access element form 3D array
# there are 2 array ---> index/Select array
# inside 2D array ----> index of 1 and 2 row
# inside 2D array ----> Select the index of the elements

import numpy as np

three_dim = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(three_dim)

print(three_dim[0,0,2])
print(three_dim[1,0,1])# access 8
print(three_dim[1,1,2])# access 12

print(three_dim[0,0:,1:])
print(three_dim[1,0:,0])


print(three_dim[0:,0:,0])
print(three_dim[0:,0:,1:])
