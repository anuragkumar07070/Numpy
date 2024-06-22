# Joining the numpy array - here for this we will pass concatenate()

import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([10,22,21,5])
arr_join = np.concatenate((arr1,arr2))
print("CONCATENATION : ",arr_join)
print()


# Joining of 2D arrays along with rows(axis =1)
import numpy as np
a = np.array([[1,2],[6,7]])
b = np.array([[10,22],[21,5]])
c = np.concatenate((a,b),axis=1)
print("CONCATENATION ALONG AXIS= 1")
print(c)
print()

# Joining array using the stack function
import numpy as np
stackf1 = np.array([1,2,3,4])
stackf2 = np.array([10,22,21,5])
stackf3 = np.array([10,12,123,15])
stackf1_op = np.stack((stackf1,stackf2,stackf3),axis=1) # axis = -1,0,1
print("Stack Join")
print(stackf1_op)
print()


# stacking along with rows : hstack()
import numpy as np
hstackf1 = np.array([1,2,3,4])
hstackf2 = np.array([10,22,21,5])
hstackf3 = np.array([10,12,123,15])
hstack_join = np.hstack((hstackf1,hstackf2,hstackf3))
print("Hstack joining")
print(hstack_join)
print()


# stacking along with columns : vstack()
vstackf1= np.array([1,2,3,4])
vstackf2 = np.array([10,22,21,5])
vstackf3 = np.array([10,12,123,15])
vstack_join = np.vstack((vstackf1,vstackf2,vstackf3))
print("vstack Joining: ")
print(vstack_join)
print()

# stacking along with height(depth)
dstack1 = np.array([1,2,3,4])
dstack2 = np.array([10,22,21,5])
dstack3 = np.array([10,12,123,15])
dstack_join = np.dstack((dstack1,dstack2,dstack3))
print("Dstack Joining")
print(dstack_join)

