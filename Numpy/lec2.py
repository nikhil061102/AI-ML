import numpy as np

arr = np.array(43)
print(arr)
print(type(arr))
arr1 = np.array([1,2,3,4])
print(arr1)
print(type(arr1))
arr2 = np.array([[1,2,3],[3,4,5]])
print(arr2)
print(type(arr2))
arr3 = np.array([[[1,2,3,4],[3,4,5,6]],[[5,6,7,8],[6,7,8,9]]])
print(arr3)
print(type(arr3))

print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)