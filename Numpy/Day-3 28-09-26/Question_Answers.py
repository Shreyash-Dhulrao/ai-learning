# Q1. Create an array containing numbers 1-24, reshape it into a 4 x 6 matrix
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

# Q2. Create a array containing only numbers that are:
#     - Greater than 10
#     - Less than 25

# Given Array:
# arr = np.array([12, 5, 18, 7, 25, 3, 30, 14, 9, 21])
# arr = arr[arr > 10]
# arr = arr[arr < 25]
# print(arr) # This will return values greater than 10 and less than 25 in the array

# Q3. Given array:
#     Replace:
#         - values < 10 → 0
#         - values 10–30 → 1
#         - values > 30 → 2

# Given array
arr = np.array([10, 25, 7, 40, 15, 3, 50, 18])

new_arr = np.zeros(len(arr), dtype=int)

new_arr[arr < 10] = 0
new_arr[(arr >= 10) & (arr <= 30)] = 1
new_arr[arr > 30] = 2

print(new_arr) # This will print the values of array in which it is added as 0, 1, 2