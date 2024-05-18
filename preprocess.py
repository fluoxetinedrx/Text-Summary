import numpy as np
from nltk import sent_tokenize
from gensim.utils import simple_preprocess
from pyvi.ViTokenizer import tokenize as word_tokenize


class Preprocessor:
    def __init__(self):
        self.word_tokenizer = word_tokenize
        self.sent_tokenizer = sent_tokenize
        self.normalizer = simple_preprocess
        with open('data/vietnamese_stopsword', 'r', encoding='utf-8') as reader:
            self.stop_words = reader.read().split("\n")

    def preprocessing(self, paragraph):
        # Chia đoạn văn thành các câu văn riêng biệt
        sentences = self.sent_tokenizer(paragraph)
        for i in range(len(sentences)):
            sentence = sentences[i]
            # chia các câu văn thành các từ riêng biệt
            sent_tokenized = self.word_tokenizer(sentence)

            # loại bỏ các stopword
            for stop_word in self.stop_words:
                if stop_word in sent_tokenized:
                    sent_tokenized = sent_tokenized.replace(stop_word, " ")

            # loại bỏ các kí tự đặc biệt, các khoảng trắng thừa
            sent_normalized = self.normalizer(sent_tokenized)
            sentences[i] = " ".join(sent_normalized)
        return sentences