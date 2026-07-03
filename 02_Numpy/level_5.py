import numpy as np 

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([3,5,6,3,2])
sum = arr1+arr2 
sub = arr1-arr2 
mul = arr1*arr2 
div = arr1/arr2
sq = arr1**2 ;
cube = arr1**3 
sqrt = np.sqrt(arr1)
expo = np.exp(arr1)
log = np.log(arr1)
sin = np.sin(arr1)
cos = np.cos(arr1)
tan = np.tan(arr1)
abs = np.absolute(arr1)
print("Sum is :" , sum) 
print("Sub is :" , sub) 
print("Mutliplication :" , mul)
print("Division :" , div.round(2))
print("Square is",sq.round(2))
print("Cube is :" , cube)
print("Square root :" , sqrt.round(2))
print("Exponent :" , expo.round(2))
print("Log :" , log.round(2))
print("sine :" , sin.round(2))
print("Cosine :" , cos.round(2))
print("Tangent :" , tan.round(2))
print("Absolute :" , abs.round(2))
print("Original array :" , arr2.round(2))
reci = np.reciprocal(arr2.astype(float)).round(2)
print("Recipocal :" , reci)
