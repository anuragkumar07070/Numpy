# difference between copy and view in numpy
# we will make a copy , change in original array. and display both.


print("Copy")

import numpy as np
a = np.array([1,2,3,4,59])
new = a.copy()
a[0] = 998  # new change 
print(a)
print(new)  # copy doesn't contain new changes once it is implemented



print()
print("view")
# now we will make a view, change original and display both

import numpy as np
arr = np.array([1,2,3,4,5])
new = arr.view()
arr[0] = 36    # new change {still you can see through view}
print(new)     # view change the value of index 0 , after changing the value of arr array
print(arr)

 