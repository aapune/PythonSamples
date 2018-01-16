import numpy as np

a = np.array([1, 2, 3])   
print(type(a))           
print(a.shape)            # "(3,)"
print(a[0], a[1], a[2])   # "1 2 3"
a[0] = 5                  
print(a)                  # "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    
print(b.shape)                     # "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # "1 2 4"