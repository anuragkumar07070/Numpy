import numpy as np
# it contains random values having any dtype 
a = np.empty((3,4)) 
print(a)

# lets gives dtype to a empty array
b = np.empty((3,2),dtype="i") # now contain only integer values
print(b)

# lets try with float data type
c = np.empty((3,4), dtype="f")
print(c)

