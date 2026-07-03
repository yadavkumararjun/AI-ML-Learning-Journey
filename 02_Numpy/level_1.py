import numpy as np 
'''
    Level 1:
 Creating Arrays (1-10)
Import NumPy with the alias np.
Create a 1D array containing numbers from 1 to 10.
Create a 2D array of shape (3,4).
Create a 3×3 array filled with zeros.
Create a 4×4 array filled with ones.
Create an identity matrix of size 5.
Create an array containing even numbers from 2 to 20.
Create an array containing numbers from 0 to 1 with step 0.1.
Create an array of 15 random integers between 1 and 100.
Create an empty array of size 8.
'''
arr1 = np.array([1,2,3,4,5,6,7,8,9,10]) ;
arr2 = np.array([
    [3,4,5,2],
    [9,1,53,2],
    [7,8,2,0]
])
arr3 = np.zeros((3,3))
arr4 = np.ones((4,4))
arr5 = np.ones((5,5))
arr6 = np.identity((5))
arr7 = np.arange(2,21,2)
arr8 = np.arange(0,1,0.1)
arr9=np.random.randint(1,101,size=15)
arr10= np.empty(8)
print(arr9)
