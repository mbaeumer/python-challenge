#!/usr/bin/python
import numpy as np

X, Y = np.loadtxt("beer.txt", skiprows=1, unpack=True)
print("Using shape")
print(X.shape[0])

print("Using column_stack to create a matrix")
matrix = np.column_stack((X, Y))
print(matrix)
print("Using shape")
print(matrix.shape[0])
print(matrix.shape[1])

print("Matrix with zeros")
matrix_with_zeros = np.zeros([3, 3])
print(matrix_with_zeros)

print("Changing the value of a cell in the matrix")
matrix_with_zeros[0,0] = 5
print(matrix_with_zeros)

print("Using matmul")
matrix_with_ones = np.ones([2,4])
print(matrix_with_ones)
result = np.matmul(matrix_with_ones, matrix)
print(result)

print("Using transpose")
print(matrix.T)

print("Using reshape")
print("before: ", X)
x = X.reshape(-1,1)
print("after: ", x)

print("Inserting a column")
matrix = np.insert(matrix, 1, 1, axis=1)
print(matrix)

print("Inserting a row")
matrix = np.insert(matrix, 1, 1, axis=0)
print(matrix)

print("Deleting a column")
matrix = np.delete(matrix, 1, axis=1)
print(matrix)

print("Deleting a row")
matrix = np.delete(matrix, 1, axis=0)
print(matrix)


