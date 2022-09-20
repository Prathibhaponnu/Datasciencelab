print("prathibha21mca034")
import numpy as np
a1=np.array([[1,2,3],[4,5,6],[5,8,7]])
a2=np.array([[3,2,1],[6,5,4],[7,8,5]])
print(np.add(a1,a2))
print(np.subtract(a1,a2))
print(np.multiply(a1,a2))
print(np.divide(a1,a2))
print(np.multiply(a1,a2))
print(a1.T)
print(a2.T)
print("sum of diagonal elements of first matrix ",sum(np.diag(a1)))
print("sum of diagonal elements of second matrix",sum(np.diag(a2)))



