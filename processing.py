from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def getVectors(text, path):
    tfidf = TfidfVectorizer()
    x_matrix = tfidf.fit_transform(text)
    y = int(path[40] == "p")

    return getDistance(x_matrix), y  # add new vectors to this array


def getDistance(matrix):
    return cosine_similarity(matrix[1], matrix[0])[0][0]

def getJdistance(matrix):
    return jacaard_score(matrix[1], matrix[0])[0][0]
