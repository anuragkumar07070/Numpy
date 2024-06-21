# Iterating array - means going through the elements one by one step by step . like a loop

# 1D Iteration 
import numpy as np
arr = np.array([1,2,3,5,6])
for i in arr:
    print(i,end=" ")

print()

# 2D iteration 
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for i in arr:
    print(i)

# Iterate over each element (Scalar)
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for i in arr:
    for j in i:
        print(j)

# 3D Iteration
import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)

for i in arr:
    for j in i:
        for k in j:
            print(k)

#**********nditer***********
import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# nditer iteration
for i in np.nditer(arr):
    print(i)

for i in np.nditer(arr[0: ,0:,:2]):
    print(i)

for i in np.nditer(arr[0:,0:,::2]):
    print(i)

for i in np.nditer(arr[0:,0:,1]):
    print(i)
