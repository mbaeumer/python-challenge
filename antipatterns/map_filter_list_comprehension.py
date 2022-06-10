

def use_map(list):
    print("\nDemo of map function")
    doubles = map(lambda num: num * 2, list)
    for number in doubles:
        print(number)

def use_filter(list):
    print("\nDemo of filter function")
    uneven = filter(lambda n: n % 2 != 0, list)
    for number in uneven:
        print(number)

def use_list_comprehension_instead_of_map(list):
    print("\nDemo of list comprehension instead of map")
    doubles = [num * 2 for num in list]
    for number in doubles:
        print(number)

def use_list_comprehension_instead_of_filter(list):
    print("\nDemo of list comprehension instead of filter")
    uneven = [num for num in list if num % 2 != 0]
    for number in uneven:
        print(number)

if __name__ == '__main__':
    values = [1, 6, 8]
    use_map(values)
    use_list_comprehension_instead_of_map(values)
    mixed_values = [1, 4, 8, 9, 13]
    use_filter(mixed_values)
    use_list_comprehension_instead_of_filter(mixed_values)