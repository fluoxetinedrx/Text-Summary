import networkx as nx
import numpy as np
from nltk import sent_tokenize
from preprocess import Preprocessor
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from sklearn.metrics.pairwise import cosine_similarity
from vectorize import Vectorizer


class Summarizer():
    def __init__(self):
        self.clearner = Preprocessor()
        self.vectorizer = Vectorizer()

    def summarize(self, paragraph, keep_sentences=5):
        # tách văn bản thành các câu riêng lẻ
        origin_sentence = sent_tokenize(paragraph)
        # tiền xử lý văn bản
        sentences = self.clearner.preprocessing(paragraph)
        # biến các câu văn thành vector cột
        sent_vectors = self.vectorizer.vectorize(sentences)  

        # chuyển vị ma trận câu
        sent_vectors_t = sent_vectors.T

        # phân rã giá trị suy biến
        U, S, VT = np.linalg.svd(sent_vectors_t)

        # Tính toán Vector Quan trọng
        saliency_vec = np.dot(np.square(S), np.square(VT))

        #Chọn Các Câu Quan trọng Nhất
        top_sentences = saliency_vec.argsort()[-keep_sentences:][::-1]
        top_sentences.sort()

        summary = " ".join([origin_sentence[i] for i in top_sentences])
        return summary, top_sentences