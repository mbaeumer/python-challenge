#!/usr/bin/python
import numpy as np

X, Y = np.loadtxt("beer.txt", skiprows=1, unpack=True)
print("Using shape")
print(X.shape[0])

print("Using column_stack to create a matrix")
matrix = np.column_stack((X, Y))
print(matrix)
print(matrix.shape[0])
print(matrix.shape[1])

print("Using transpose")
print(matrix.T)

print("Using reshape")
print("before: ", X)
x = X.reshape(-1,1)
print("after: ", x)


