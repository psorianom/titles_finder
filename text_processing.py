__author__ = 'Pavel Soriano'

import nltk

def find_top_ngram(tokens, n=10):
    from nltk.collocations import BigramCollocationFinder, BigramAssocMeasures
    from nltk.tokenize import word_tokenize

    if not isinstance(tokens, list):
        tokens = word_tokenize(tokens)
        tokens = [t for t in tokens if len(tokens) > 3 ]
    ignored_words = nltk.corpus.stopwords.words('english')
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    # tokenks_filtered = [t for t in tokens if len(t)>3]
    finder = BigramCollocationFinder.from_words(tokens)

    finder.apply_freq_filter(3)
    finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)
    oo = finder.nbest(bigram_measures.raw_freq, n)
    pass

