import numpy as np 

arr1= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_matrix = arr1.reshape(3,4)
flat_matrix = new_matrix.reshape(12)
print("Reshaped from 1D to 2D \n" ,new_matrix)
print("Flat matrix \n" , flat_matrix )
col_matrix = new_matrix.reshape(1 ,12)
row_matrix = new_matrix.reshape(12 ,1)
print("Column Matrix \n" ,col_matrix)
print("Row Matrix \n" ,row_matrix)

#transpose
trans_matrix = new_matrix.transpose()
print("Transposed matrix \n" , trans_matrix)

stacked_vertical = np.vstack((arr1,arr2))
stacked_horizontal= np.hstack((arr1,arr2))
print(stacked_vertical)
print(stacked_horizontal)
part1, part2, part3 = np.split(arr1, 3)
print("Part 1:", part1)
print("Part 2:", part2)
print("Part 3:", part3)
left_side, right_side = np.split(new_matrix, 2, axis=1)
print("Left Matrix:\n", left_side)
print("\nRight Matrix:\n", right_side)
