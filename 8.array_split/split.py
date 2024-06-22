# split - break or divide the array into sub arrays
# using array_split fn

import numpy as np
arr = np.array([1,2,3,4,5,6])
a = np.array_split(arr,3) # (arr_name , no of divisions)
print(a)


# Now we wil split this array in 4 parts 
# question is , how can we divide an array with 6 element
# can be divded into 4 four parts >> let see
import numpy as np
arr = np.array([1,2,3,4,5,6])
a = np.array_split(arr,4) # (arr_name , no of divisions)
print(a)


# split into array
import numpy as np
arr = np.array([1,2,3,4,5,6])
a = np.array_split(arr,3) # (arr_name , no of divisions)
print(a[0])
print(a[1])
print(a[2])

#*************2D Array*****************
import numpy as np
arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
a = np.array_split(arr,3)
print(a)

# spilt the 2D array into three 2D arrays


