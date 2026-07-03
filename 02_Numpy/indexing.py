import numpy as np 


#Element Acccessing by index 

# arr_1d =np.arange(12)
# print(arr_1d[2:8])
# print(arr_1d) 

arr_2d = np.array([[1,2,3,4],   # indexing start from 0 in both row and column
                   [8,4,2,5],
                   [4,3,5,2]
                    ])
# print("Specific Element0 " , arr_2d[1,2])
# print("Entire row :",arr_2d[2])  # arr_2d[row , column]  keep in mind
# print("Entire colum:",arr_2d[:,3])

# sorting 
print("Sorted 2d matrix by row" , np.sort(arr_2d , axis=1))   # axis = 1 => row 
print("Sorted 2d matrix by column" , np.sort(arr_2d , axis=0)) # axia = 0 => column
unsorted = np.array([3,1,4,2,5,6,5])
print("Sorted array :" , np.sort(unsorted)) ;


#Filter 
number = np.arange(15)
even_number = number[number%2==0]
print("Even Number" ,even_number)
odd_number = number[number%2!=0]
print("Odd Number :", odd_number)


#Filter with mask 
mask= number>5 ;  # it store the boolean value true/false for each value depending on expression . 
# print("Mask :" , mask)
print("Number greater then 5 :" , number[mask])


# fancy indexing vs np.where()
indices = [1,2,9,4,5]  # stores index value 
print(number[indices])
where_result = np.where(number>5)
print(where_result)
print("NP Where :", number[where_result])  

