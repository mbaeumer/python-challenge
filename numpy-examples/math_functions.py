#!/usr/bin/python
import numpy as np

X, Y = np.loadtxt("beer.txt", skiprows=1, unpack=True)
print(X[0:5])
print(Y[0:5])

print("Using the average function")
print(np.average(X))

print("Using the max function")
print(np.max(X))

print("Using the min function")
print(np.min(X))

print("Using the sum function")
print(np.sum(X))

print("Using the argmax function")
print(np.argmax(X))

print("Using the argmin function")
print(np.argmin(X))


print("Using the round function")
in_array = [.5538, .2448]
print(np.round(in_array, decimals=3))

print("Using the maximum function")
print(np.maximum(X, Y))

print("Using the minimum function")
print(np.minimum(X, Y))

print("Using the sqrt function")
print(np.sqrt(X))

print("Using the square function")
print(np.square(X))

