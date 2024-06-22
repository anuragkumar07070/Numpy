# Accessing the 2D array element
# Accessing 2D array element is like row and columns game
# or you can say matrix

import numpy as np

two_dim = np.array([[1,2,3],[4,5,6]])
print(two_dim)

print(two_dim[0,2])# 0 is for Row and 1 Stands for index of row
print(two_dim[0,0])

print(two_dim[0,1:])
print(two_dim[0,:2])
print(two_dim[0,:3])
print(two_dim[ 0,0:])

print(two_dim[0:,1])
print(two_dim[:2,1:])
print(two_dim[0:,0:])
print(two_dim[0:,:2])
