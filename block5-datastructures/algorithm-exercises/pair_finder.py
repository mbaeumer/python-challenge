

# list of strings
# find all pairs

def find_pairs_v1():
    words = ["1", "2", "3", "4"]
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            print("%s-%s" % (words[i], words[j]))

def find_pairs_v2(words):
    for first_index in range(len(words)):
        for second_index in range(first_index + 1, len(words)):
            print("%s-%s" % (words[first_index], words[second_index]))

def find_pairs_v3(words):
    pairs = []
    for first_index in range(len(words)):
        for second_index in range(first_index + 1, len(words)):
            pairs.append((words[first_index], words[second_index]))
    return pairs

def show_all_pairs_v1(pairs):
    for pair in pairs:
        print("%s-%s" % (pair[0], pair[1]))

def show_all_pairs_v2(pairs):
    for pair in pairs:
        print(f"{pair[0]}-{pair[1]}")


if __name__ == '__main__':
    find_pairs_v1()
    words = ["1", "2", "3", "4"]
    pairs = find_pairs_v3(words)
    show_all_pairs_v1(pairs)
    show_all_pairs_v2(pairs)
