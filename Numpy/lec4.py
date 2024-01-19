import numpy as np

arr = np.array(43)
arr1 = np.array([1,2,3,4])
arr2 = np.array([[1,2,3],[3,4,5]])
arr3 = np.array([[[1,2,3,4],[3,4,5,6]],[[5,6,7,8],[6,7,8,9]]])

print(arr)
print(arr1[1])
print(arr1[-1]) # last element
print(arr1[-2]) # second last element 
print(arr2[1][2] == arr2[1,2])
print(arr3[1][1][2] == arr3[1,1,2])