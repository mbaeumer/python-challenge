
def bad(filename):
    file_obj = open(filename, 'r')
    data = file_obj.read()
    file_obj.close()
    print(data)

def good(filename):
    with open(filename, 'r') as file_obj:
        data = file_obj.read()

    print(data)

if __name__ == '__main__':
    print("Bad")
    bad("persons.txt")

    print("Good")
    good("persons.txt")
