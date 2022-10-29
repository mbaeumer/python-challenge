from functools import reduce

def multiply(value):
    return value * value

def map_demo():
    list = [1,2,3,4]
    mapped_list = map(multiply, list)

    for item in mapped_list:
        print(item)

def even_number(value):
    return value % 2 == 0

def filter_demo():
    list = [1, 2, 3, 4]
    even_numbers = filter(even_number, list)

    for item in even_numbers:
        print(item)

def add(a, b):
    return a+ b

def reduce_demo():
    list = [1, 2, 3, 4]
    sum = reduce(add, list)
    print("The sum of all values in the list: %d" % sum)


if __name__ == '__main__':
    map_demo()
    filter_demo()
    reduce_demo()