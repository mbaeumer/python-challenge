import nltk
from word_pair import WordPair
from word_pair_count import WordPairCount

def count_co_occurrences():
    sentences = ["This sentence is about cats and dogs",
                 "This sentence is about mice and hamsters",
                 "This sentence is about cats and hamsters"]
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    all_words = []
    for sentence in tokenized_sentences:
        all_words.extend(sentence)
    unique_words = list(set(all_words))
    word_pairs = find_permutations(unique_words)
    word_pair_counts = []

    for sentence in tokenized_sentences:
        for word_pair in word_pairs:
            if sentence.count(word_pair.first) > 0 and sentence.count(word_pair.second) > 0:
                update_word_pair_count(word_pair_counts, word_pair)

    for word_pair_count in word_pair_counts:
        print("%s and %s: %d" % (word_pair_count.word_pair.first, word_pair_count.word_pair.second, word_pair_count.count))

def update_word_pair_count(word_pair_counts, word_pair):
    found = False
    for wpc in word_pair_counts:
        if wpc.word_pair.first == word_pair.first and wpc.word_pair.second == word_pair.second:
            wpc.count += 1
            found = True

    if not found:
        word_pair_counts.append(WordPairCount(word_pair, 1))

def find_permutations(words):
    permutations = []

    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            permutations.append(WordPair(words[i], words[j]))
    return permutations

if __name__ == '__main__':
    count_co_occurrences()