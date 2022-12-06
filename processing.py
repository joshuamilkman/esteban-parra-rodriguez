from nltk import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def getData(text, path, N):
    tfidf = TfidfVectorizer()
    T_matrix = tfidf.fit_transform(text) # contains (originalText, text of new file)
    T = getDistance(T_matrix)
    J = getJaccard(text)

    if int(path[40] == "p"):
        Z = "plagiarized"
    else:
        Z = "clean"

    return N, J, T, Z  # add new vectors to this array


def getDistance(matrix):
    return cosine_similarity(matrix[0], matrix[1])[0][0]

def jaccard_set(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union


def getJaccard(group):
    original = word_tokenize(group[0])
    comparison = word_tokenize(group[1])
    return jaccard_set(original, comparison)
