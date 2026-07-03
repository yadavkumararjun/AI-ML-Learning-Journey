import numpy as np


arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[0])
print(arr[arr.size-1])
print(arr[0:5])
print(arr[::2])

matrix=np.array([
    [10 ,20 ,30 ,40],
    [90 ,15 ,25 ,35],
    [50 ,60 ,70 ,80]
 ])
print(matrix)
print(matrix[1])
print(matrix[:,3])
print(matrix[matrix.shape[0]-1])
print(matrix[:,matrix.shape[1]-1])
print(matrix[0:2 , 0:2])
matrix[0:1 , 0:1]=100
print(matrix)
new_matrix= np.where(matrix%2 !=0 ,-1,matrix)
print(new_matrix)

matrix_mixed = np.array([
    [-10,  25, -30,  42],
    [ 55,  -8,  70, -12],
    [ -3,  99, -15,  88]
])
neg_to_zero_matrix = np.where(matrix_mixed<0 ,0,matrix_mixed)
print(neg_to_zero_matrix)

print(matrix[matrix>50])
print(matrix[matrix%2==0])

'''
Level 3: Indexing and Slicing (21-35)
Print the first element.
Print the last element.
Print the first five elements.
Print every alternate element.
Reverse an array.
Print the second row of a matrix.
Print the third column.
Print the last row.
Print the last column.
Extract a 2×2 submatrix.
Replace the first element with 100.
Replace all odd numbers with -1.
Replace all negative numbers with 0.
Select elements greater than 50.
Select even numbers only.
'''