from collections import Counter

def create_counter_from_list():
    counter = Counter(['a', 'b', 'a'])
    print(counter)

def create_counter_with_values():
    counter = Counter(a=2, b=1)
    print(counter)

def create_counter_from_string():
    counter = Counter('aba')
    print(counter)

# delete counter
# elements
# most common
# subtract
# update
# counter arithmetic

def get_count():
    counter = Counter('aba')
    print(counter['a'])

def set_count():
    counter = Counter('aba')
    counter['a'] = 5
    print(counter['a'])

def delete_counter():
    counter = Counter('aba')
    del counter['b']
    print(counter)

def get_elements():
    counter = Counter('aba')
    print(counter.elements())

def most_common():
    counter = Counter('aba')
    print(counter.most_common())

def subtract():
    counterA = Counter('aba')
    counterB = Counter('bca')
    counterA.subtract(counterB)
    print(counterA)

    counterA = Counter('aba')
    counterB = Counter('abb')
    counterA.subtract(counterB)
    print(counterA)

def update():
    counterA = Counter('aba')
    counterB = Counter('abb')
    counterA.update(counterB)
    print(counterA)

def intersection():
    counterA = Counter('aba')
    counterB = Counter('abb')
    result = counterA & counterB
    print(result)

def union():
    counterA = Counter('aba')
    counterB = Counter('abb')
    result = counterA | counterB
    print(result)




# source: https://www.digitalocean.com/community/tutorials/python-counter-python-collections-counter
if __name__ == '__main__':
    create_counter_from_list()
    create_counter_with_values()
    create_counter_from_string()

    get_count()
    set_count()
    delete_counter()
    get_elements()
    most_common()
    subtract()
    update()
    intersection()
    union()