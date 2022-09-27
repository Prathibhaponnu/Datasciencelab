print("Prathibha21mca034")
import numpy as np
a=np.random.randint(10,size=(3,3))
print(a)
inverse=np.linalg.inv(a)
print("inverse of matrix",inverse)
rank=np.linalg.matrix_rank(a)
print("rank of matrix",rank)
determinant=np.linalg.det(a)
print("deteminant of matrix",determinant)
new_a=a.reshape(-1)
print("transformed 1-d array",new_a)
v,w=np.linalg.eig(a)
print("eigen values:",v)
print("eigen vectors",w)



