
def find_occurrences_in_string(whole_string, search_string):
    indices = []
    pos = 0
    while pos + len(search_string) <= len(whole_string):
        if whole_string[pos:pos + len(search_string)] == search_string:
            indices.append(pos)
        pos = pos + 1
    return indices

def show_index_list(indices, search_string, whole_string):
    print("Indices where '%s' is found in '%s'" % (search_string, whole_string))
    for index in range(len(indices)):
        print(index)

if __name__ == '__main__':
    indices = find_occurrences_in_string("aaa", "a")
    show_index_list(indices, "a", "aaa")
    indices = find_occurrences_in_string("aaa", "aa")
    show_index_list(indices, "aa", "aaa")

