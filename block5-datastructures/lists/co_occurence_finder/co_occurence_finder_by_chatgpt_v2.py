# python how to find which words occur together in multiple sentences

#You can use natural language processing (NLP) tools to identify which words occur together in multiple sentences.
#For example, you can use the NLTK library for Python to create a co-occurrence matrix, which shows which words
#occur together in the same context. You can also use scikit-learns
#CountVectorizer to create a bag-of-words vectorizer to identify which words appear together in multiple sentences.


import nltk

# Create a list of sentences
sentences = [
    "This is the first sentence",
    "This is the second sentence",
    "This is the third sentence"
]

# Create a list to store the co-occurrence matrix
co_occurrences = []

# Iterate over each sentence
for sentence in sentences:
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)

    # Create a co-occurrence matrix for the sentence
    co_occurrences.append(nltk.FreqDist(nltk.bigrams(tokens)))

# Print the co-occurrence matrix
print(co_occurrences)