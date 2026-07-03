import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,2,5,9,1])

combined = np.concat((arr1,arr2))  # pass array as tuple
print(combined) ;
print("Compatibility:" , arr1.shape==arr2.shape)

# add row or column 
original = np.arange(1, 26).reshape(5, 5)
new_row = np.arange(1,6).reshape(1,5)
new_col = np.arange(11,17).reshape(6,1)
# print(original)
print(new_row)
print(new_col)
with_new_row = np.vstack((original,new_row))
print(with_new_row)
with_new_col = np.hstack((with_new_row , new_col))
# print("final matrix :" , with_new_col)


# Delete row and column 
# 1. Delete the 2nd row (index 1)
final_matrix = with_new_col
matrix_no_row = np.delete(final_matrix , 1 , axis=0) #  (matrix , index , row(0)/col(1) )
print("With deleted row :")
print(matrix_no_row)
print("with deleted col :")
matrix_no_col = np.delete(final_matrix , 3 , axis = 1)
print(matrix_no_col)

