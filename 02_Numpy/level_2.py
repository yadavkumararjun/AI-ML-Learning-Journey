import numpy as np 

arr= np.array([1,2,3,4,5,6,7])
arr2= np.arange(0 ,1 , 0.1 )
bool_arr = np.array([1,2,0,-3,62] , dtype =bool)
shape = arr.shape
dim = arr.ndim
size=arr.size
data_type = arr.dtype
arr.dtype='float64'
arr2.dtype='int64'
item_size = arr.itemsize
mem= arr.nbytes
print(shape)
print(dim)
print(size)
print(data_type)
print(item_size)
print(mem)
print(bool_arr)

'''
Level 2:
Array Properties (11-20)
Find the shape of a given array.
Find the number of dimensions.
Find the total number of elements.
Find the data type of an array.
Convert an integer array into float.
Convert a float array into integer.
Find the item size of each element.
Find the total memory occupied by the array.
Create an array with dtype bool.
Check whether an array is C-contiguous.
'''