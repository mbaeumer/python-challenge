

def read_key_from_file(filename):
    key = ""
    try:
        with open(filename, 'r') as file:
            for line in file:
                key = line
                break
    except FileNotFoundError:
        print("The file does not exist!")
        raise FileNotFoundError
    return key

