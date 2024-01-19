import numpy as np

arr = np.array(43)
arr1 = np.array([1,2,3,4])
arr2 = np.array([[1,2,3],[3,4,5]])
arr3 = np.array([[[1,2,3,4],[3,4,5,6]],[[5,6,7,8],[6,7,8,9]]])

print(arr.shape)
print(arr1.shape)
print(arr2.shape)
print(arr3.shape)

# Reshaping arrays
arr1_reshape = arr1.reshape(2,2)
print(arr1_reshape.shape)
print(arr1_reshape)
arr3_reshape = arr3.reshape(8,2)
print(arr3_reshape.shape)
print(arr3_reshape)

# Flatten n-D arrays
flatten_arr3 = arr3_reshape.reshape(-1)
print(flatten_arr3.shape)
print(flatten_arr3)