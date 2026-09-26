import numpy as np

''' Methods from which we can check about array in numpy
1. np.shape: It is used to check the shape of the array (i.e. 2,3 or 3,4 etc)
2. np.size: It is used to check the total count of the array 
3. np.ndim: It is use to check the dimensions of the array (i.e. 1 or 2 or 3)
4. np.dtype: It is use to check the data type present in the array (int, float, str etc)
'''

# ----------- Size Method -----------
# arr = np.array([20,30,10,50,40])
# print(arr.size) # It will return 5 as the elements in the array is 5

# ----------- Shape Method -----------
# arr = np.array([[30,20,50],[10,40,60]])
# print(arr.shape) # It will return 2,3 as it contains 2 rows and 3 columns

# ----------- Ndim Method -----------
arr = np.array([[30,20,50],[10,40,60]])
print(arr.ndim) # It will return 2, because it is a 2d array