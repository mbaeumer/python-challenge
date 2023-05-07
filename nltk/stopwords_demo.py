from nltk.corpus import stopwords

def show_stopword_languages():
    print(stopwords.fileids())

def show_stopwords_of_language(language):
    try:
      print(stopwords.words(language))
    except OSError:
      print("Could not find specified language")

def demo_raw():
    print(stopwords.raw('swedish'))

if __name__ == '__main__':
    show_stopword_languages()
    show_stopwords_of_language('swedish')
    show_stopwords_of_language('german')
    show_stopwords_of_language('abc')
    demo_raw()
