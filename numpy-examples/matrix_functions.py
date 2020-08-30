#!/usr/bin/python
import numpy as np

X, Y = np.loadtxt("pizza.txt", skiprows=1, unpack=True)
print(X.shape[0])
print(X.T)
print(np.sum(X))
matrix = np.column_stack((X, Y))
print(matrix)
print(matrix.T)
