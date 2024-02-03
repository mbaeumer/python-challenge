import nltk

def demo_bigrams():
    sentence = "This is the sentence"
    tokens = nltk.word_tokenize(sentence)
    bigrams = nltk.bigrams(tokens)
    everygram = nltk.everygrams(tokens)
    nltk.ev
    print(list(bigrams))
    print(list(everygram))

def demo_co_occurence_matrix():
    sentence = "This is the sentence"
    tokens = nltk.word_tokenize(sentence)
    co_occurrences = nltk.FreqDist(nltk.bigrams(tokens))
    print(co_occurrences)

if __name__ == '__main__':
    demo_bigrams()
    demo_co_occurence_matrix()