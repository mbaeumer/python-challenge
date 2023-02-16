
#def init_list():

def simple_comprehension():
    list = "abcdefghijklmnopqrstuvwxyz"
    [print(x) for x in list]

def find_vowels_without_comprehension():
    list = "bcdefghijklmnopqrstuvwxyza"
    vowels = "aeiou"
    found = []
    for c in list:
        if c in vowels:
            found.append(c)
    print("Found vowels in the following order")
    for c in found:
        print(c)

def find_vowels_with_comprehension():
    list = "bcdefghijklmnopqrstuvwxyza"
    vowels = "aeiou"
    found = [c for c in list if c in vowels]

    print("Found vowels in the following order")
    for c in found:
        print(c)

if __name__ == '__main__':
    simple_comprehension()
    find_vowels_without_comprehension()
    find_vowels_with_comprehension()