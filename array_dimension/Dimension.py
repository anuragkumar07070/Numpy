# Dimension in Arrays 

# 0D array
import numpy as np 
zero_dim =np.array(23)
print(zero_dim)


# 1D array
import numpy as np 
one_dim = np.array([1,2,3,4,6])
print(one_dim)

# 2D array
import numpy as np
two_dim = np.array([[2,3,4],[1,27,6]])
print(two_dim)

# 3D Array
import numpy as np 
three_dim = np.array([[[1,2,4],[8,6,4]],[[4,3,7],[24,523,3]]])
print(three_dim)

# 10D array
import numpy as np
ten_dim = np.array([1,24,43,46],ndmin=10)
print(ten_dim)


# How to check dimesion of the array :ndim 
print("Dimension of the array")
print(zero_dim.ndim)
print(one_dim.ndim)
print(two_dim.ndim)
print(three_dim.ndim)