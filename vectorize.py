import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


class Vectorizer:
    """
        vectorize list of sentence
        return row vector
    """

    def __init__(self):

        self.count_vectorizer = CountVectorizer(ngram_range=(1, 3))
        self.tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 3))

    def vectorize(self, sentences, mode = "count" ):

        if mode == "count":
            return self.count_vectorizer.fit_transform(sentences).toarray()
        elif mode == "tfidf":
            return self.tfidf_vectorizer.fit_transform(sentences).toarray()
