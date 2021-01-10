#!/usr/bin/python

import numpy as np

def start():
    array = init_array()
    print(array)
    sort(array, 0, len(array))
    print(array)

def init_array():
    array = np.empty([5])
    array[0] = 5
    array[1] = 3
    array[2] = 17
    array[3] = 9
    array[4] = 2

    return array

def sort(array, low, high):

    if low < high:
        pi = partition(array, low, high)
        sort(array, low, pi - 1)
        sort(array, pi + 1, high)


def partition(array, low, high):
    pivot = array[high - 1]

    i = low - 1
    j = low
    while j <= high - 1:
        if array[j] < pivot:
            i = i + 1
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
        j = j +1
    temp = array[i + 1]
    array[i + 1] = array[high - 1]
    array[high - 1] = temp

    return i + 1

if __name__ == '__main__':
    start()