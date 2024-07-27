import numpy as np

a = np.array([1,2,3])
print(a.shape)
print(a)

b = np.array([[1,2],[1,21]])
print(b)
print(b.shape)

c =np.array([12,21])
print(c.shape)


d = np.array([[[1,2,1],[1,3,2]],[[1,2,3],[14,54,3]]])
print(d)
print(d.shape)
f = d.reshape(3,2,2)
print(f)

import numpy as np

a = np.array([[1,2,3,4,5],[4,6,8,9,10]])
for i in np.nditer(a[0:,2:]):
	print(i)