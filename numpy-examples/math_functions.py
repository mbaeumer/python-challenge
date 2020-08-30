#!/usr/bin/python
import numpy as np

X, Y = np.loadtxt("pizza.txt", skiprows=1, unpack=True)
print(X[0:5])
print("Using the average funnction")
print(np.average(X))
print(np.average(X)- Y)

print("Using the round function")
in_array = [.5538, .2448]
print(np.round(in_array))

print("Using the round_ function")
in_array = [.5538, .2448]
print(np.round_(in_array, decimals=3))

print("Using the maximum function")
print(np.maximum(X, Y))

print("Using the minimum function")
print(np.minimum(X, Y))

print("Using the sqrt function")
print(np.sqrt(X))

print("Using the square function")
print(np.square(X))

print("Using the sum function")
print(np.sum(X))
