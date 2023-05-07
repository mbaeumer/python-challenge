
def is_same(number, aList, anotherList):
    print("Example #" + str(number))
    print("aList: ", aList)
    print("anotherList: ", anotherList)
    print(aList == anotherList)

if __name__ == '__main__':
    list1 = ['A', 'B', 'C', 'B', 'B', 'C', 'B', 'A']
    list2 = ['A', 'B', 'C', 'B', 'B', 'C', 'B', 'A']
    is_same(1, list1, list2)

    list1 = ['A', 'B', 'C', 'B', 'B', 'C', 'B', 'A']
    list2 = ['A', 'B', 'B', 'C', 'B', 'C', 'B', 'A']
    is_same(2, list1, list2)

    list2 = ['A', 'B', 'C', 'B', 'B', 'C', 'B']
    is_same(3, list1, list2)

    list2 = ['A', 'B', 'C', 'B', 'B', 'C', 'B', 'B']
    is_same(4, list1, list2)

    list2 = ['B', 'A', 'C', 'B', 'B', 'C', 'B', 'A']
    is_same(5, list1, list2)


