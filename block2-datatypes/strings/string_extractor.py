

def extract_string():
    sample_string = "key1: value1\nkey2: value2\nkey3: value3\nkey4: value4\n"
    key_index = sample_string.find("key2")
    remainder = sample_string[key_index:len(sample_string)]
    line_break_index = remainder.find("\n")
    value = remainder[0:line_break_index]
    return value

if __name__ == '__main__':
    print(extract_string())
