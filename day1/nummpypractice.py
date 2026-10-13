#nummpypractice
import numpy as np
a = np.array([1, 2, 3,], dtype = 'int16')
b = np.array([[9.0, 8.9, 1.3],[1.5,2.7,2.6]])
print(a.ndim) # prints the number of dimensions of array a
print(b.shape) # prints the shape of array b
print(a.dtype) # prints the data type of array a
print(a.itemsize) # prints the size in bytes of each element of array a
print(a.size) # prints the total number of elements in array a
print(b.itemsize) # prints the size in bytes of each element of array b

r = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]], dtype=np.int16)
print(r)
print(r.shape)
print(r[1,0]) # prints the element at row 1, column 0 of array r
print(r[0,:]) # prints all elements of row 0 of array r
#print(r[startindex:endindex:stepsize]) selects elements from x to y with a step size
print(r[0, 1:7:1])
r[1,4] = 10
print(r) # prints the updated array r after changing the element at row 1, column 4 to 10
r[:,3] = 5
print(r) # prints the updated array r after changing all elements in column 3 to


