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
    chosen = 1
    while chosen < len(array):
        compare_index = chosen - 1
        selected_value = array[chosen]
        switched = False
        compare_value = array[compare_index]
        while selected_value < compare_value and compare_index >=0:
            #if selected_value < array[compare_index]:
            array[compare_index + 1] = array[compare_index]
                #array[chosen] = array[compare_index]
                #array[compare_index] = temp
            switched = True
            compare_index = compare_index - 1
            compare_value = array[compare_index]
        if switched:
            array[compare_index + 1] = selected_value
        chosen = chosen + 1
    return array

if __name__ == '__main__':
    start()
