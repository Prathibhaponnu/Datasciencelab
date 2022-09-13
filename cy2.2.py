import numpy as np
a=np.array([[1,2,3],[4,5,6]],dtype=complex)
print("Number of rows and columns:",a.shape)
print("Dimension of an array:",a.ndim)
print("Before reshape",a)
print("After reshape",a.reshape(3,2))
