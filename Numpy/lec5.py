import numpy as np

arr = np.array(43)
arr1 = np.array([1,2,3,4])
arr2 = np.array([[1,2,3],[3,4,5]])
arr3 = np.array([[[1,2,3,4],[3,4,5,6]],[[5,6,7,8],[6,7,8,9]]])

for i in arr1:
    print(i)

for i in arr2:
    print(i)

for i in arr2:
    for j in i:
        print(j)