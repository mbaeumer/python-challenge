from itertools import count
from itertools import cycle
from itertools import repeat
from itertools import accumulate
from itertools import dropwhile
from itertools import filterfalse
from itertools import takewhile
from itertools import product
from itertools import combinations
from itertools import permutations



def demo_count():
    iterator = count(10)
    print(list(next(iterator) for _ in range(100)))

def demo_cycle():
    iterator = cycle('ABCD')
    aList = list(next(iterator) for _ in range(len('ABCD')))
    print(aList)

def demo_repeat():
    iterator = repeat(10, 5)
    aList = list(next(iterator) for _ in range(5))
    print(aList)

def demo_accumulate():
    iterator = accumulate([1,2,3])
    aList = list(next(iterator) for _ in range(3))
    print(aList)

def demo_dropwhile():
    originalList = [1,2,4,5,6]
    iterator = dropwhile(lambda x: x%2 > 0, originalList)
    for item in iterator:
        print(item)

def demo_filterfalse():
    originalList = [1, 2, 4, 5, 6]
    iterator = filterfalse(lambda x: x%2==0, originalList)
    for item in iterator:
        print(item)

def demo_takewhile():
    originalList = [1, 2, 4, 5, 6]
    iterator = takewhile(lambda x: x % 2 > 0, originalList)
    for item in iterator:
        print(item)

def demo_product():
    iterator = product('ABCD')
    for item in iterator:
        print(item)

def demo_product_with_repeat():
    iterator = product('ABCD', repeat=2)
    for item in iterator:
        print(item)

def demo_permutations():
    iterator = permutations('ABCD')
    for item in iterator:
        print(item)

def demo_combinations():
    print("combinations")
    iterator = combinations('ABCD', 2)
    for item in iterator:
        print(item)

if __name__ == '__main__':
    demo_count()
    demo_cycle()
    demo_repeat()
    demo_accumulate()
    demo_dropwhile()
    demo_filterfalse()
    demo_takewhile()
    demo_product()
    demo_product_with_repeat()
    demo_permutations()
    demo_combinations()