# reshape - changing the dimension/shape of an array


# Reshaping 1D to 2D 
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_arr = arr.reshape(4,3)
print(arr)
print(new_arr)


# Reshaping 1D to 3D 
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_arr = arr.reshape(2,3,2)
print(arr)
print(new_arr)


# return copy or view
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(4,2))