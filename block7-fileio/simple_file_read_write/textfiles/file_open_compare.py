

def open_with(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print("The file does not exist!")

def open_old_school(filename):
    try:
        file = open(filename, "r")
        for line in file:
            print(line)
        file.close()
    except FileNotFoundError:
        print("The file does not exist!")


if __name__ == '__main__':
    open_old_school("persons.txt")
    open_with("persons.txt")