# Data Type in Numpy

# i for integer
# b for boolean
# u for unsigned integer
# f for float
# c for complex float
# m for timedelta
# M for datetime
# O for object
# S for string
# U for unicode string
# V - memory 

# To check the datatype of Numpy {dtype}
import numpy as np
arr = np.array([1,2,2000])
print(arr.dtype)


# To check the datatype of Numpy {dtype}
import numpy as np
arr = np.array(["apple","banana","grapes"])
print(arr.dtype)


# create array with a defined data type
import numpy as np
arr = np.array([1,2,3,4],dtype="S")
print(arr)
print(arr.dtype)

# now we will create an array with data type of 4 byte int
import numpy as np
arr = np.array([1,2,20,3493],dtype="i4")
print(arr)
print(arr.dtype)


# if a type is given in which the element cannnot 
# be casted then numpy will raise error, what if a value 
# cannot be converted?
# ****Example***********
"""import numpy as np
arr = np.array(["a","1","2"],dtype="i")
print(arr.dtype)"""

#  Converting data type in existing array - astype()
import numpy as np
a = np.array([1.4,2.2,3.7,4.9])
print(a)
print("Datatype of a: ",a.dtype)
b = a.astype('i')
print(b)
print("Data type of b: ",b.dtype)
