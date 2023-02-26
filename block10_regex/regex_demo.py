import re

#split
def split_demo(string):
    print(re.split(r"\W", string))

#match
def match_demo(string):
    print(re.match(r"\d+", string))

#search
def search_demo():
    print(re.search(r"\w+", "This is a sentence with characters and 0 numbers"))

#findall
def findall_demo():
    print(re.findall(r"\d", "5446 is my number"))

def one_character_of_demo():
    print(re.search(r"[a-d]", "abecd"))

def one_character_except_demo():
    print(re.search(r"[^a-d]", "abecd"))

if __name__ == '__main__':
    string = "This is a sentence with characters and 0 numbers"
    start_with_number = "5446 is my number"
    split_demo(string)
    split_demo(start_with_number)
    match_demo(string)
    match_demo(start_with_number)
    search_demo()
    findall_demo()
    one_character_of_demo()
    one_character_except_demo()
