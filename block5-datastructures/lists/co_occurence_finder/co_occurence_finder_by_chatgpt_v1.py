# Import the necessary libraries
import collections
import nltk

# Define the sentences
sentences = ["This sentence is about cats and dogs",
             "This sentence is about mice and hamsters",
             "This sentence is about cats and hamsters"]

# Tokenize the sentences
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

# Find the co-occurring words
co_occurrences = collections.Counter()

for sentence in tokenized_sentences:
    for word in sentence:
        co_occurrences[word] += 1

# Print the co-occurring words
for word, count in co_occurrences.most_common():
    if count > 1:
        print(word, count)