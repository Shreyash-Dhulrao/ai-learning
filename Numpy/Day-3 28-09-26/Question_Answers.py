# Create an array containing numbers 1-24, reshape it into a 4 x 6 matrix
#   - Find the sum of each row.
#   - Find the sum of each column.
#   - Find the maximum value in each row.
import numpy as np

arr = np.arange(1,25)

arr = arr.reshape(4, 6)

# ------------ Sum of rows ------------
# for i in range(len(arr)):
#     new_arr = np.sum(arr[i])
#     print(new_arr) # This will print the sum of every value of the row

# ------------ Sum of Columns ------------
# new_arr = np.sum(arr, axis=0)
# print(new_arr) # This will print sum of all column values 

# ------------ Max Value in Row ------------
# for i in range(len(arr)):
#     new_arr = np.max(arr[i])
#     print(new_arr) # This will print maximum value present in the particular row of array
