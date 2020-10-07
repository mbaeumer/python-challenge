#!/usr/bin/python

from numpy import array
from numpy import empty 
from numpy import zeros
from numpy import ones

print("Demo of numpy")
a = array([3,5,9])
print("array with 3 pre-set numbers")
print(a)

empty_array = empty([3])
print("array with no pre-set numbers")
print(empty_array)

array_with_zeros = zeros([3])
print("array with 3 zeros")
print(array_with_zeros)

array_with_ones = ones([3])
print("array with 3 ones")
print(array_with_ones)
