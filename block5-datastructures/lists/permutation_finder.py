
def find_permutations():
    words = ['hamsters', 'cats', 'This', 'is', 'about', 'dogs', 'mice', 'sentence', 'and']
    permutations = []

    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            permutations.append(words[i] + "+" + words[j])


if __name__ == '__main__':
    find_permutations()