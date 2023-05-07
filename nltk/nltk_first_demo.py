# Important
# install nltk using pip3
# download corporas using the interpreter






from nltk.corpus import gutenberg
from nltk.corpus import alpino
#from nltk import corpus.gutenberg

def show_alpino_details():
    print("Fileids: ", alpino.fileids())
    print("Words: ", alpino.words())

if __name__ == '__main__':
    print(gutenberg.fileids())
    print(alpino.fileids())
    print(gutenberg.words())
    gut = gutenberg
    print("File IDs: %d" % len(gut.fileids()))
    print("Raw: %d" % len(gut.raw()))
    print("Words: %d" % len(gut.words()))
    #print("Sentencess: %d" % len(gut.sents()))
    print("Sentencess: %d" % len(alpino.sents()))
    show_alpino_details()