#!/usr/bin/python
import numpy as np

def start():
    array = init_array()
    print(array)
    sorted_arrray = sort(array)
    print(sorted_arrray)

def init_array():
    array = np.empty([5])
    array[0] = 5
    array[1] = 3
    array[2] = 17
    array[3] = 9
    array[4] = 2

    return array

def sort(array):
    swapped = True
    while swapped:
        swapped = False
        index = 0
        while index < len(array) - 2:
            if array[index] > array[index + 1]:
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp
                swapped = True
            index = index + 1

    return array

if __name__ == '__main__':
    start()
