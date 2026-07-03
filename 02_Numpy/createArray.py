import numpy as np 
import time

#vector
vector = np.array([1,2,3,4,5])
print("vector :" , vector)
print("Dimension" ,vector.ndim)
print("Size" , vector.size)
print("DataType :",vector.dtype)

matrix = np.array([
    [5,6,7,8],
    [9,1,4,2]
])
print("Matrix :" , matrix)
print("Dimension" ,matrix.ndim)
print("Size" , matrix.size)
print("DataType :",matrix.dtype)

tenser = np.array(
    [
        [[1,2,3,4],[5,6,7,8]] ,
        [[12,43,23,45] ,[78,45,23,22]]
    ]
)
print("tenser :", tenser)
print("Dimension" ,tenser.ndim)
print("Size" , tenser.size)
print("DataType :",tenser.dtype)
