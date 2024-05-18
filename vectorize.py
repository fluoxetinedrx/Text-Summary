import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


class Vectorizer:
    """
        vector hoá danh sách các câu
        trả về row vector
    """
    def __init__(self):
        self.count_vectorizer = CountVectorizer(ngram_range=(1, 3))

    def vectorize(self, sentences):
            return self.count_vectorizer.fit_transform(sentences).toarray()
