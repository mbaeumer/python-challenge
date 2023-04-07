import re

#split
def split_demo(string):
    return re.split(r"\W", string)

#match
def match_demo(string):
    return bool(re.match(r"\d+", string))

def match_span_demo(string):
    return re.match(r"\d+", string).span()

#search
def search_demo(string):
    return re.search(r"\w+", string)

#findall
def findall_demo(string):
    return re.findall(r"\d", string)

def one_character_of_demo(string):
    return re.search(r"[a-d]", string)

def one_character_except_demo(string):
    return re.search(r"[^a-d]", string)

def valid_minute_demo(time_string):
    match = re.match(r"^[0-5]",time_string)
    return match

def valid_minute_group_demo(time_string):
    print("minute_group")
    match = re.match(r"^[0-5]",time_string)
    return match.group()


if __name__ == '__main__':
    string = "This is a sentence with characters and 0 numbers"
    start_with_number = "5446 is my number"
    print(string + "->", split_demo(string))
    print(start_with_number + "->", split_demo(start_with_number))
    print(string + "->", match_demo(string))
    print(start_with_number + "->", match_demo(start_with_number))
    print(start_with_number + "->", match_span_demo(start_with_number))
    print(string + "->", search_demo(string))
    print(start_with_number + "->", findall_demo(start_with_number))
    print("abecd ->", one_character_of_demo("abecd"))
    print("abecd ->", one_character_except_demo("abecd"))
    print(valid_minute_demo(""))
    print(valid_minute_demo("0"))
