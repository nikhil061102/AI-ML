import numpy as np

arr = np.array(43)
arr1 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
arr2 = np.array([[1,2,3,4,5],[3,4,5,6,7]])
arr3 = np.array([[[1,2,3,4],[3,4,5,6]],[[5,6,7,8],[6,7,8,9]]])

print(arr1[1:5])
print(arr1[2:7])
print(arr1[:4])
print(arr1[5:])
print(arr1[1:7:2])
print(arr1[1:-1])
print(arr1[:-5:2])
print(arr1[1:7:-2])
print(arr1[:-5:-2])

print(arr2[1,1:4])
print(arr2[0,0:3])