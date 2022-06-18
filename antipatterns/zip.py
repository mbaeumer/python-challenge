

def bad():
    print("Bad example")
    numbers = [1,2,3]
    chars = ['A','B','C']

    for index in range(len(numbers)):
        print(numbers[index],chars[index])

def good():
    print("Good example")
    numbers = [1, 2, 3]
    chars = ['A', 'B', 'C']

    for number, char in zip(numbers, chars):
        print(number, char)

if __name__ == '__main__':
    bad()
    good()